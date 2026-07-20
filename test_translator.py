import unittest
from translator import resolve_language_code, translate_text

class TestTranslator(unittest.TestCase):
    def test_resolve_language_code_known(self):
        """Test resolving known language names to ISO codes."""
        self.assertEqual(resolve_language_code("french"), "fr")
        self.assertEqual(resolve_language_code("HINDI"), "hi")
        self.assertEqual(resolve_language_code("  spanish "), "es")

    def test_resolve_language_code_unknown(self):
        """Test resolving unknown/already coded languages."""
        self.assertEqual(resolve_language_code("fr"), "fr")
        self.assertEqual(resolve_language_code("xyz"), "xyz")

    def test_translate_text_basic(self):
        """Test a basic translation (Google Translate backend requires internet)."""
        # "hello" in French is usually "bonjour"
        result = translate_text("hello", "fr", "en")
        self.assertTrue(isinstance(result, str))
        self.assertIn("bonjour", result.lower())

if __name__ == "__main__":
    unittest.main()
