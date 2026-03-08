SYSTEM_PROMPT = """
You are an expert Social Media Manager and Copywriter. 
Your task is to analyze brands and generate high-performing tweets.
"""

BRAND_ANALYSIS_PROMPT = """
Analyze the brand '{brand_name}' in the '{industry}' industry.
Return a JSON object with:
1. "tone": A single word (e.g., Bold, Witty).
2. "audience": A brief description of the target audience.
3. "characteristics": 4 bullet points describing the brand's voice.
"""

TWEET_GENERATION_PROMPT = """
Based on the brand analysis: {analysis}
Objective: {objective}
Product: {product_description}

Generate 10 tweets. For each tweet, provide:
1. Category (Engaging, Promo, Info, or Witty)
2. Tweet text (with hashtags and emojis)
3. Engagement Score (0-100)
4. Character count

Return as a JSON list of objects.
"""