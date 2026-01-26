import os
import re

# Directory containing blog articles
blog_dir = r'c:\Users\ostap\OneDrive\Documents\GitHub\blackstone\blog'

# List of blog article files (excluding index.html)
blog_files = [
    'kitchen-backsplash-ballantyne.html',
    'bathroom-remodel-lake-norman.html',
    'outdoor-living-huntersville.html',
    'walk-in-shower-concord.html',
    'sauna-installation-matthews.html',
    'luxury-bathroom-ballantyne.html',
    'custom-shower-lake-norman.html',
    'steam-shower-huntersville.html',
    'bathroom-tile-concord.html',
    'master-bathroom-matthews.html',
    'tile-installation-charlotte.html'
]

# Improved styles with better readability
improved_styles = '''    <style>
        :root {
            --primary-color: #2B3A42;
            --secondary-color: #C6A056;
            --text-color: #1a1a1a;
            --light-text-color: #FFFFFF;
            --light-bg-color: #F8F9FA;
            --border-color: #DEE2E6;
            --font-heading: 'Oswald', sans-serif;
            --font-body: 'Open Sans', sans-serif;
            --container-max-width: 1200px;
            --border-radius: 5px;
            --box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: var(--font-body);
            line-height: 1.8;
            color: var(--text-color);
            background-color: #ffffff;
        }

        .container {
            max-width: var(--container-max-width);
            margin: 0 auto;
            padding: 0 20px;
        }

        .site-header {
            background-color: var(--light-text-color);
            padding: 15px 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.07);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary-color);
            text-transform: uppercase;
            text-decoration: none;
        }

        .back-link {
            color: var(--secondary-color);
            text-decoration: none;
            font-weight: 700;
            transition: color 0.3s ease;
        }

        .back-link:hover {
            color: var(--primary-color);
        }

        h1,
        h2,
        h3 {
            font-family: var(--font-heading);
            margin-bottom: 1.5rem;
            line-height: 1.3;
            font-weight: 700;
            text-transform: uppercase;
        }

        h1 {
            font-size: clamp(2rem, 5vw, 3rem);
            margin-top: 2rem;
            color: var(--primary-color);
        }

        h2 {
            font-size: clamp(1.75rem, 4vw, 2.25rem);
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            color: #1a2730;
            font-weight: 700;
        }

        h3 {
            font-size: 1.4rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
            font-weight: 700;
        }

        p {
            margin-bottom: 1.25rem;
            color: #2c3e50;
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .article-header {
            background: linear-gradient(135deg, #1a2730 0%, var(--primary-color) 100%);
            color: var(--light-text-color);
            padding: 70px 0 50px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .article-header h1 {
            color: var(--light-text-color);
            margin-bottom: 1rem;
        }

        .article-meta {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.05rem;
            margin-top: 15px;
            font-weight: 500;
        }

        .article-content {
            max-width: 900px;
            margin: 0 auto;
            padding: 70px 20px;
            background-color: #ffffff;
        }

        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin: 50px 0;
        }

        .benefit-card {
            background-color: #ffffff;
            padding: 35px;
            border-radius: var(--border-radius);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 2px solid #f0f0f0;
        }

        .benefit-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
            border-color: var(--secondary-color);
        }

        .benefit-card h3 {
            color: var(--primary-color);
            font-size: 1.25rem;
            margin-top: 0;
            margin-bottom: 1rem;
        }

        .benefit-card p {
            color: #555;
            font-size: 1rem;
            line-height: 1.7;
        }

        .benefit-icon {
            font-size: 3.5rem;
            color: var(--secondary-color);
            margin-bottom: 20px;
        }

        .cta-section {
            background: linear-gradient(135deg, #1a2730 0%, var(--primary-color) 100%);
            padding: 70px 20px;
            text-align: center;
            margin-top: 50px;
        }

        .cta-section h2 {
            color: var(--light-text-color);
            margin-top: 0;
        }

        .cta-section p {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.15rem;
        }

        .cta-button {
            display: inline-block;
            padding: 16px 35px;
            border-radius: var(--border-radius);
            font-family: var(--font-heading);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-decoration: none;
            transition: all 0.3s ease;
            background-color: var(--secondary-color);
            color: var(--light-text-color);
            margin: 10px;
            font-size: 1rem;
        }

        .cta-button:hover {
            background-color: #b08f4d;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(198, 160, 86, 0.4);
        }

        .site-footer {
            background-color: var(--primary-color);
            color: rgba(255, 255, 255, 0.9);
            padding: 50px 0 30px;
            text-align: center;
        }

        .site-footer h3 {
            color: var(--light-text-color);
            margin-top: 0;
        }

        .site-footer a {
            color: var(--secondary-color);
            text-decoration: none;
            transition: color 0.3s ease;
            font-weight: 500;
        }

        .site-footer a:hover {
            color: #d4ac6e;
        }

        .local-area {
            background: linear-gradient(135deg, #e8f4f8 0%, #d4e9f2 100%);
            padding: 35px;
            border-left: 5px solid var(--secondary-color);
            margin: 40px 0;
            border-radius: var(--border-radius);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .local-area h3 {
            color: var(--primary-color);
            margin-bottom: 15px;
            margin-top: 0;
        }

        .local-area p {
            color: #2c3e50;
            font-size: 1.05rem;
        }

        ol, ul {
            color: #2c3e50;
            font-size: 1.1rem;
            line-height: 2;
        }

        ol li, ul li {
            margin-bottom: 12px;
        }

        strong {
            color: var(--primary-color);
            font-weight:700;
        }
    </style>'''

# Improved footer template
improved_footer = '''    <footer class="site-footer">
        <div class="container">
            <div style="margin-bottom: 25px;">
                <h3 style="color: var(--light-text-color); font-size: 1.4rem; margin-bottom: 20px; font-weight: 700;">Contact BlackStone Construction</h3>
                <p style="margin: 12px 0; font-size: 1.1rem;">
                    <i class="fas fa-phone"></i> <a href="tel:+14125836880" style="color: var(--secondary-color); font-weight: 600;">(412) 583-6880</a>
                </p>
                <p style="margin: 12px 0; font-size: 1.1rem;">
                    <i class="fas fa-envelope"></i> <a href="mailto:quote@blackstoneclt.com" style="color: var(--secondary-color); font-weight: 600;">quote@blackstoneclt.com</a>
                </p>
                <p style="margin: 12px 0; font-size: 1.1rem;">
                    <i class="fab fa-instagram"></i> <a href="https://www.instagram.com/blackstone_construction_design/" target="_blank" style="color: var(--secondary-color); font-weight: 600;">@blackstone_construction_design</a>
                </p>
            </div>
            <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.8);">&copy; <span id="current-year"></span> BlackStone Construction & Design LLC. All Rights Reserved.</p>
            <p style="margin-top: 15px; font-size: 0.95rem;">
                <a href="../index.html">Home</a> |
                <a href="../blog/">Blog</a> |
                <a href="../index.html#services">Services</a> |
                <a href="../index.html#contact">Contact</a>
            </p>
        </div>
    </footer>'''

# Process each blog file
for filename in blog_files:
    filepath = os.path.join(blog_dir, filename)
    
    if os.path.exists(filepath):
        print(f"Updating {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace styles (from <style> to </style>)
        content = re.sub(
            r'    <style>.*?</style>',
            improved_styles + '\n    </style>',
            content,
            flags=re.DOTALL
        )
        
        # Replace footer (from <footer to </footer>)
        content = re.sub(
            r'    <footer class="site-footer">.*?</footer>',
            improved_footer,
            content,
            flags=re.DOTALL
        )
        
        # Write updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {filename}")
    else:
        print(f"✗ File not found: {filename}")

print("\n✅ All blog articles updated with improved readability and contact info!")
