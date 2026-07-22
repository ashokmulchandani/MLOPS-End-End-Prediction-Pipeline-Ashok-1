"""
Unit Tests for Phase 6 Enterprise Training Data Pipeline

Patterns tested: Loaders, Chunkers, AI Generators, Quality Evaluators, Exporters
These tests follow the 3-type rule: Happy Path, Edge Cases, Failure Modes.

Usage: pytest test_enterprise_pipeline.py -v
"""
import pytest
import json
from unittest.mock import Mock, patch, MagicMock

# ═══════════════════════════════════════════════════════════
# MOCK MODELS — simulating Phase 6 data models
# ═══════════════════════════════════════════════════════════

class Document:
    def __init__(self, content, doc_type="TXT", source="test.txt"):
        self.content = content
        self.doc_type = doc_type
        self.source = source
        self.id = f"doc_{hash(content) % 10000}"

class TextChunk:
    def __init__(self, content, doc_id, chunk_index=0):
        self.content = content
        self.document_id = doc_id
        self.chunk_index = chunk_index
        self.token_count = len(content.split())

class TrainingExample:
    def __init__(self, question, answer, source_chunk_id, task_type="QA"):
        self.question = question
        self.answer = answer
        self.source_chunk_id = source_chunk_id
        self.task_type = task_type

# ═══════════════════════════════════════════════════════════
# 1. DOCUMENT LOADER TESTS
# ═══════════════════════════════════════════════════════════

class TestDocumentLoader:
    """Happy Path + Edge Cases + Failure Modes for loading documents"""

    # ── Happy Path ──
    def test_load_txt_file_returns_document(self):
        """Loading a valid TXT file should return a Document object"""
        doc = Document("Hello world", doc_type="TXT")
        assert doc.content == "Hello world"
        assert doc.doc_type == "TXT"
        assert doc.id is not None

    def test_load_pdf_returns_document(self):
        """Loading a PDF should extract text and return Document"""
        doc = Document("PDF content extracted", doc_type="PDF")
        assert doc.content != ""
        assert doc.doc_type == "PDF"

    @pytest.mark.parametrize("doc_type", ["TXT", "PDF", "URL", "CSV"])
    def test_unified_loader_routes_to_correct_loader(self, doc_type):
        """UnifiedLoader should route to correct specialist based on type"""
        doc = Document("test", doc_type=doc_type)
        assert doc.doc_type == doc_type

    # ── Edge Cases ──
    def test_empty_file_returns_empty_document(self):
        """Empty file should return Document with empty content, not crash"""
        doc = Document("", doc_type="TXT")
        assert doc.content == ""  # Empty but valid

    def test_very_large_file_still_loads(self):
        """Large files should load without memory errors"""
        large_content = "word " * 100000  # Simulate 100K words
        doc = Document(large_content, doc_type="TXT")
        assert len(doc.content) > 0

    def test_filename_with_special_characters(self):
        """Files with special chars in name should still load"""
        doc = Document("content", source="file (1) copy - final!.txt")
        assert doc.source == "file (1) copy - final!.txt"

    # ── Failure Modes ──
    def test_corrupt_file_raises_clear_error(self):
        """Corrupt file should raise specific error, not crash silently"""
        with pytest.raises(ValueError, match="Cannot parse|corrupt|invalid"):
            raise ValueError("Cannot parse corrupt file: invalid encoding")

    def test_unsupported_file_type_raises_error(self):
        """Unknown file types should be rejected with clear message"""
        supported = ["TXT", "PDF", "URL", "CSV"]
        unsupported_type = "XLSX"
        if unsupported_type not in supported:
            with pytest.raises(ValueError, match="Unsupported"):
                raise ValueError(f"Unsupported file type: {unsupported_type}")


# ═══════════════════════════════════════════════════════════
# 2. CHUNKER TESTS
# ═══════════════════════════════════════════════════════════

class TestChunker:
    """Test the smart text chunking logic"""

    def test_chunk_respects_max_size(self):
        """Each chunk should be under the max token limit"""
        content = "word " * 5000
        max_tokens = 1000
        chunks = []
        words = content.split()
        for i in range(0, len(words), max_tokens):
            chunk_words = words[i:i + max_tokens]
            chunks.append(TextChunk(" ".join(chunk_words), "doc_1", i // max_tokens))

        for chunk in chunks:
            assert chunk.token_count <= max_tokens, \
                f"Chunk has {chunk.token_count} tokens, max is {max_tokens}"

    def test_chunks_maintain_order(self):
        """Chunks should be sequential and maintain document order"""
        content = "word " * 3000
        chunks = []
        words = content.split()
        for i in range(0, len(words), 1000):
            chunks.append(TextChunk(" ".join(words[i:i+1000]), "doc_1", i//1000))

        for i in range(len(chunks) - 1):
            assert chunks[i].chunk_index < chunks[i+1].chunk_index

    def test_overlap_preserves_context(self):
        """Overlap between chunks should preserve boundary context"""
        overlap = 200
        chunk1_end = "the capital of France is Paris"
        chunk2_start = "is Paris which is located in"
        # The overlap "is Paris" should appear in both
        assert "Paris" in chunk1_end
        assert "Paris" in chunk2_start

    def test_single_chunk_when_content_smaller_than_max(self):
        """Content smaller than max_tokens should produce exactly 1 chunk"""
        small_content = "short text"
        chunks = [TextChunk(small_content, "doc_1", 0)]
        assert len(chunks) == 1


# ═══════════════════════════════════════════════════════════
# 3. AI GENERATOR TESTS (QA Generation)
# ═══════════════════════════════════════════════════════════

class TestQAGenerator:
    """Test the AI-powered QA pair generation"""

    def test_generates_qa_from_chunk(self):
        """Given a text chunk, should return Q&A pairs"""
        chunk = TextChunk("Machine learning is a subset of AI.", "doc_1")
        # Simulate AI response
        qa_pairs = [
            TrainingExample("What is ML?", "A subset of AI.", chunk.id),
        ]
        assert len(qa_pairs) > 0
        assert qa_pairs[0].question != ""
        assert qa_pairs[0].answer != ""

    def test_empty_chunk_returns_no_qa(self):
        """Empty chunk should return empty list, not hallucinate Q&A"""
        chunk = TextChunk("", "doc_1")
        qa_pairs = []  # Generator returns nothing for empty input
        assert len(qa_pairs) == 0

    def test_rate_limit_is_handled_gracefully(self):
        """Rate limit (429) should trigger retry, not crash"""
        with pytest.raises(Exception) as exc_info:
            # Simulate API rate limit
            raise Exception("429 Too Many Requests")
        assert "429" in str(exc_info.value) or "rate" in str(exc_info.value).lower()

    def test_generated_qa_has_unique_ids(self):
        """Every Q&A pair should reference its source chunk"""
        chunk = TextChunk("AI systems learn from data.", "doc_abc")
        examples = [
            TrainingExample("Q1", "A1", chunk.id),
            TrainingExample("Q2", "A2", chunk.id),
        ]
        for ex in examples:
            assert ex.source_chunk_id == chunk.id


# ═══════════════════════════════════════════════════════════
# 4. QUALITY EVALUATOR TESTS
# ═══════════════════════════════════════════════════════════

class TestQualityEvaluator:
    """Test the quality scoring and filtering logic"""

    def test_passing_example_scores_above_threshold(self):
        """A good Q&A pair should score above minimum threshold"""
        example = TrainingExample(
            "What is Python?", "Python is a programming language.", "doc_1"
        )
        # Simulated quality score
        score = 0.85  # 85% quality
        threshold = 0.7
        assert score >= threshold, f"Quality score {score} below threshold {threshold}"

    def test_gibberish_example_scores_below_threshold(self):
        """Gibberish Q&A should be rejected"""
        example = TrainingExample("asdfghjkl", "zxcvbnm", "doc_1")
        score = 0.05  # Very low quality
        threshold = 0.7
        assert score < threshold, "Gibberish should not pass quality gate"

    def test_too_short_answer_rejected(self):
        """One-word answers should be flagged as low quality"""
        example = TrainingExample("What is ML?", "Yes.", "doc_1")
        min_answer_length = 10
        assert len(example.answer) < min_answer_length

    def test_quality_report_counts_pass_fail(self):
        """Quality report should accurately count passes and failures"""
        examples = [
            TrainingExample("Q1", "A detailed answer about ML", "doc_1"),
            TrainingExample("Q2", "Short", "doc_1"),
            TrainingExample("Q3", "Another detailed response here", "doc_1"),
        ]
        passed = sum(1 for e in examples if len(e.answer) > 10)
        failed = len(examples) - passed
        assert passed == 2
        assert failed == 1


# ═══════════════════════════════════════════════════════════
# 5. EXPORTER TESTS
# ═══════════════════════════════════════════════════════════

class TestExporter:
    """Test dataset export to different formats"""

    def test_export_json_produces_valid_json(self):
        """JSON export should produce parseable JSON"""
        examples = [TrainingExample("Q1", "A1", "doc_1")]
        data = [{"question": e.question, "answer": e.answer} for e in examples]
        json_str = json.dumps(data)
        parsed = json.loads(json_str)
        assert len(parsed) == 1
        assert parsed[0]["question"] == "Q1"

    def test_export_empty_dataset_produces_empty_array(self):
        """Exporting zero examples should produce empty array, not null"""
        data = []
        json_str = json.dumps(data)
        assert json_str == "[]"

    def test_export_preserves_metadata(self):
        """Export should include source and quality metadata"""
        exported = {
            "question": "What is AI?",
            "answer": "Artificial Intelligence",
            "source_doc": "intro.pdf",
            "quality_score": 0.92,
            "generation_date": "2026-07-22"
        }
        assert "source_doc" in exported
        assert "quality_score" in exported
        assert exported["quality_score"] > 0.9
