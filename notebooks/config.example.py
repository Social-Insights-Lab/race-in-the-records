"""Project configuration. Copy to notebooks/config.py; keys are read from the environment."""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# API keys (set in your shell or a local .env; never commit them)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "")
XAI_API_KEY = os.environ.get("XAI_API_KEY", "")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

# Paths
NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks')
OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs')
RAW_DATA_DIR = os.path.join(BASE_DIR, 'datasets/01_raw')
OCR_DATA_DIR = os.path.join(BASE_DIR, 'datasets/02_ocr')
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'datasets/03_processed')
REDACTED_DATA_DIR = os.path.join(BASE_DIR, 'datasets/04_redacted')
PRIMARY_DATA = os.path.join(BASE_DIR, 'datasets/02_ocr/police_narratives_complete.json')
DATA_2022 = os.path.join(BASE_DIR, 'datasets/02_ocr/2022_narratives.json')
ALL_YEARS_DATA = os.path.join(BASE_DIR, 'datasets/02_ocr/police_narratives_all_years.json')
BW_DATASET = os.path.join(BASE_DIR, 'datasets/03_processed/bw_dataset_with_splits.json')
CLEAN_DATA = os.path.join(BASE_DIR, 'datasets/03_processed/data_clean.json')
DEDUP_DATA = os.path.join(BASE_DIR, 'datasets/03_processed/data_deduplicated.json')
REDACTED_DATA = os.path.join(BASE_DIR, 'datasets/04_redacted/data_redacted.json')
BALANCED_RESULTS = os.path.join(BASE_DIR, 'datasets/04_redacted/balanced_results_1000.json')
EXCEL_FILE = os.path.join(BASE_DIR, 'Police/Copy of RPD SRR Data Project.xlsx')
OCR_DIR = os.path.join(BASE_DIR, 'datasets/02_ocr')
ANALYSIS_OUT = os.path.join(BASE_DIR, 'outputs/analysis')
CLASS_OUT = os.path.join(BASE_DIR, 'outputs/classification')
PIPELINE_OUT = os.path.join(BASE_DIR, 'outputs/pipelines')
LOG_ODDS_OUT = os.path.join(BASE_DIR, 'outputs/analysis/log_odds_fixed.csv')
ESCALATION_OUT = os.path.join(BASE_DIR, 'outputs/analysis/escalation_v2.json')
RACE_INFER_OUT = os.path.join(BASE_DIR, 'outputs/analysis/race_inference_v2.json')
GEN_DIR = os.path.join(BASE_DIR, 'generations')
GEN_NARRATIVES_DIR = os.path.join(BASE_DIR, 'generations/narratives')
GEN_IMAGES_DIR = os.path.join(BASE_DIR, 'generations/images')
GEN_SKETCHES_DIR = os.path.join(BASE_DIR, 'generations/character_sketches')
GEN_NARRATIVES_V2 = os.path.join(BASE_DIR, 'generations/narratives/generation_v2.jsonl')
GEN_IMAGES_V2 = os.path.join(BASE_DIR, 'generations/images/image_character_v2.jsonl')
GEN_ANALYSIS = os.path.join(BASE_DIR, 'generations/narratives/generation_analysis_full.json')
COUNTERFACTUAL_DATA = os.path.join(BASE_DIR, 'generations/narratives/counterfactual_pairs.json')
COUNTERFACTUAL_OUT = os.path.join(BASE_DIR, 'generations/narratives/counterfactual_pairs.json')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
BERT_DIR = os.path.join(BASE_DIR, 'models/bert')
MISTRAL_DIR = os.path.join(BASE_DIR, 'models/mistral')
FASTTEXT_MODEL = os.path.join(BASE_DIR, 'models/fasttext/fasttext_narratives.bin')
FIGURES_DIR = os.path.join(BASE_DIR, 'outputs/figures')

# Models, constants
CLAUDE_FAST = 'claude-haiku-4-5-20251001'
CLAUDE_SMART = 'claude-sonnet-4-6'
GPT4O = 'gpt-5.4-2026-03-05'
GPT4O_MINI = 'gpt-4o-mini'
OPENAI_MINI = 'gpt-4o-mini'
GEMINI_FLASH = 'gemini-3-flash-preview'
GEMINI_PRO = 'gemini-2.5-pro'
DEEPSEEK_CHAT = 'deepseek-chat'
MISTRAL_LARGE = 'mistral-large-latest'
MISTRAL_SMALL = 'mistral-small-latest'
OLLAMA_BASE_URL = 'http://localhost:11434'
OLLAMA_GEMMA = 'gemma3:12b'
OLLAMA_LLAMA = 'llama3.1:8b'
OLLAMA_MISTRAL = 'mistral:7b-instruct'
OLLAMA_PORTS = {'gemma3-12b': 11435, 'llama3.1-8b': 11436, 'mistral-7b': 11437}
JUDGE_MODELS = [('claude-sonnet', 'anthropic', 'claude-sonnet-4-6'), ('gpt-5.4', 'openai', 'gpt-5.4-2026-03-05'), ('gemini-pro', 'gemini', 'gemini-2.5-pro')]
GENERATION_MODELS = [('gpt-5.4', 'openai', 'gpt-5.4-2026-03-05'), ('claude-sonnet', 'anthropic', 'claude-sonnet-4-6'), ('gemini-flash', 'gemini', 'gemini-3-flash-preview'), ('deepseek-v3', 'deepseek', 'deepseek-chat'), ('mistral-large', 'mistral', 'mistral-large-latest'), ('gemma3-12b', 'ollama', 'gemma3:12b'), ('llama3.1-8b', 'ollama', 'llama3.1:8b'), ('mistral-7b', 'ollama', 'mistral:7b-instruct')]
OPEN_MODELS = {'roberta-base': 'roberta-base', 'bert-base': 'bert-base-uncased', 'deberta-v3-small': 'microsoft/deberta-v3-small', 'distilbert': 'distilbert-base-uncased', 'legal-bert': 'nlpaueb/legal-bert-base-uncased'}
RANDOM_SEED = 42
RACES = ['Black', 'White']
N_BOOTSTRAP = 5000
RACE_MAPPING = {'B': 'Black', 'W': 'White', 'w': 'White', 'H': 'Hispanic', 'A': 'Asian', 'O': 'Other', 'U': 'Unknown'}
RESISTANCE_SCALE = {'none': 0, 'compliant': 0, 'no resistance': 0, 'cooperative': 0, 'no active resistance': 0, 'verbal resistance': 1, 'verbal refusal': 1, 'verbal refusal to comply': 1, 'verbal refusal to leave': 1, 'refused verbal commands': 1, 'refused commands': 1, 'refused to leave': 1, 'non-compliance with verbal commands': 1, 'non-compliance': 1, 'yelling': 1, 'uncooperative': 1, 'failing to adhere to verbal commands': 1, 'verbal threats': 1, 'verbal resistance (failing to adhere to verbal commands)': 1, 'avoiding custody': 2, 'passive resistance': 2, 'walking away': 2, 'refused to exit vehicle': 2, 'pulling away': 2, 'tensing body': 2, 'going limp': 2, 'dead weight': 2, 'avoiding custody (running/walking away)': 2, 'avoiding custody (running away)': 2, 'active resistance': 3, 'fleeing': 3, 'running away': 3, 'fled on foot': 3, 'fleeing on foot': 3, 'fleeing/running away': 3, 'foot pursuit': 3, 'running': 3, 'assaultive': 4, 'aggressive': 4, 'fighting': 4, 'physical resistance': 4, 'striking': 4, 'kicking': 4, 'biting': 4, 'spitting': 4, 'attempted assault': 4, 'armed': 5, 'weapon': 5, 'deadly force': 5, 'armed resistance': 5}
# Person names were removed from this list for the public release.
ROCHESTER_STOPWORDS = {'ave', 'avenue', 'bay', 'blvd', 'boulevard', 'brooks', 'brown', 'chili', 'clifford', 'clinton', 'court', 'ct', 'culver', 'davis', 'dewey', 'dr', 'drive', 'east', 'genesee', 'glendale', 'goodman', 'green', 'hall', 'highland', 'hudson', 'jefferson', 'king', 'lake', 'lane', 'lexington', 'ln', 'lopez', 'lyell', 'main', 'martin', 'monroe', 'north', 'northeast', 'northwest', 'norton', 'ontario', 'parkway', 'pkwy', 'pl', 'place', 'portland', 'rd', 'ridge', 'road', 'rochester', 'south', 'southeast', 'southwest', 'st', 'state', 'street', 'thurston', 'walker', 'way', 'west', 'young'}


for _d in (OUTPUTS_DIR, ANALYSIS_OUT, CLASS_OUT, PIPELINE_OUT, FIGURES_DIR,
           GEN_NARRATIVES_DIR, GEN_IMAGES_DIR, GEN_SKETCHES_DIR):
    os.makedirs(_d, exist_ok=True)


def ollama_url(model_key, endpoint='api/chat'):
    """Return the full URL for a given Ollama model key on its dedicated GPU port."""
    return f'http://localhost:{OLLAMA_PORTS.get(model_key, 11434)}/{endpoint}'
