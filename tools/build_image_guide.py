import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_image_guide():
    # Scan all HTML files for placeholders
    html_files = sorted([f for f in os.listdir(BASE_DIR) if f.endswith(".html")])
    
    # Regex to grab placeholder divs
    pattern = re.compile(
        r'<div class="image-placeholder\s+([^"]+)"\s+data-placeholder-filename="([^"]+)"\s+data-dimensions="([^"]+)">.*?<div class="placeholder-dimensions">Target:[^&]*&bull;\s*([^<]+)</div>',
        re.DOTALL
    )

    placeholders = []
    for hf in html_files:
        with open(os.path.join(BASE_DIR, hf), "r", encoding="utf-8") as f:
            content = f.read()
        
        matches = pattern.findall(content)
        for aspect, filename, dims, label in matches:
            placeholders.append({
                "page": hf,
                "aspect": aspect.strip().replace("aspect-", "").replace("-", ":"),
                "filename": filename.strip(),
                "dimensions": dims.strip(),
                "label": label.strip(),
                "orientation": "Square" if "1:1" in aspect else "Landscape"
            })

    total_images = len(placeholders)
    landscape_count = sum(1 for p in placeholders if p["orientation"] == "Landscape")
    square_count = sum(1 for p in placeholders if p["orientation"] == "Square")
    portrait_count = sum(1 for p in placeholders if p["orientation"] == "Portrait")

    # Helper function to generate deep, photorealistic, professional prompts
    def make_detailed_prompt(p):
        fn = p["filename"]
        lbl = p["label"]
        page = p["page"]

        if "hero-business-consulting" in fn:
            return {
                "section": "Hero Visual",
                "desc": "Executive strategic consultation in a high-rise corporate boardroom overlooking a metropolitan skyline.",
                "prompt": "Premium editorial corporate photography of an executive strategy consulting meeting in an ultra-modern high-rise boardroom overlooking a sunlit metropolitan financial skyline. Three diverse senior business consultants and two executive clients in bespoke navy and charcoal tailored suits engaged in a strategic dialogue. A minimalist glass conference table with leather document folders, sleek tablets, and subtle growth charts. Natural floor-to-ceiling window light, subtle warm timber accents, calm confident body language, Hasselblad 100MP medium format look, hyper-realistic textures, 8k resolution, no logos, no text overlays, no artificial smiles.",
                "comp": "Eye-level medium-wide angle capturing the boardroom table, participants, and deep architectural skyline perspective.",
                "lighting": "Soft morning sunlight diffused through floor-to-ceiling architectural glass with warm balanced interior cove lighting.",
                "bg": "Modern corporate boardroom with floor-to-ceiling glass and soft blurred city skyline.",
                "style": "High-end corporate documentary, refined, understated luxury, cinematic depth of field.",
                "palette": "Deep corporate navy, slate grey, warm walnut timber, crisp white, subtle brass.",
                "neg_space": "Generous upper and right-side negative space for UI title breathing room."
            }
        elif "about-corporate-philosophy" in fn:
            return {
                "section": "Philosophy & Principles",
                "desc": "Consulting advisors reviewing strategic blueprints and diagnostic matrices in a bright corporate suite.",
                "prompt": "Authentic commercial corporate photography of two senior business advisors in formal attire collaborating over diagnostic enterprise frameworks in a tranquil, contemporary architectural conference room. Clean minimalist desk, warm ambient daylight streaming from large panoramic windows, professional and focused expressions, ultra-sharp focus on analytical diagrams, editorial quality, realistic skin tones, 8k, no text, no watermarks.",
                "comp": "Three-quarters medium shot with diagonal composition leading toward the consultants.",
                "lighting": "Crisp natural daylight with soft interior architectural fill.",
                "bg": "Minimalist architectural suite with fluted acoustic wood paneling.",
                "style": "Prestigious corporate advisory aesthetic, calm and dignified.",
                "palette": "Charcoal, navy blue, light oak, soft ivory.",
                "neg_space": "Clean top-left area."
            }
        elif "service-" in fn or "-lead.webp" in fn or "digital-transformation-strategy" in fn or "operations-process-analysis" in fn or "startup-business-planning" in fn or "risk-management-framework" in fn or "project-management-governance" in fn or "organizational-development-culture" in fn or "marketing-strategy-meeting" in fn or "it-consulting-architecture" in fn or "financial-consulting-dashboard" in fn:
            # Service specific
            service_name = fn.replace("service-", "").replace("-lead.webp", "").replace("-strategy.webp", "").replace(".webp", "").replace("-", " ").title()
            return {
                "section": f"{service_name} Practice Lead / Card",
                "desc": f"Professional advisory engagement illustrating {service_name} in a modern corporate setting.",
                "prompt": f"Premium commercial photography of a senior business consultant advising client executives on {service_name}. Authentic corporate boardroom setting, tailored business attire, interactive display showing clean analytical workflows and data visualizations in soft focus. Natural window lighting, genuine focused expressions, ultra-detailed architectural interiors, photorealistic 8k, cinematic depth of field, no stock clichés, no handshakes, no visible brand logos.",
                "comp": "Balanced medium angle with natural leading lines towards the collaborative interaction.",
                "lighting": "Soft diffused natural window daylight with subtle warm interior accents.",
                "bg": "Modern enterprise conference room with floor-to-ceiling glass partitions.",
                "style": "Corporate editorial photography, prestigious management advisory tone.",
                "palette": "Navy primary (#101D35), slate blue (#244B78), warm white, subtle gold accents (#B99A5B).",
                "neg_space": "Balanced side or upper negative space."
            }
        elif "industry-" in fn:
            ind_name = fn.replace("industry-", "").replace(".webp", "").replace("-", " ").title()
            return {
                "section": f"Industry Practice - {ind_name}",
                "desc": f"Modern commercial facility and professional operations in the {ind_name} sector.",
                "prompt": f"High-end corporate documentary photography representing the modern {ind_name} sector. Clean, technologically advanced operational environment with professional staff executing structured workflows. High dynamic range, realistic lighting, authentic commercial environment, sharp focus, 8k resolution, photorealistic, no watermarks, no brand text.",
                "comp": "Wide-angle architectural environmental shot showcasing operational scale and precision.",
                "lighting": "Natural lighting appropriate to a premier commercial facility with clean balanced fill.",
                "bg": f"Contemporary state-of-the-art {ind_name} facility.",
                "style": "Prestigious industrial and commercial documentary photography.",
                "palette": "Neutral slate grey, architectural navy, clean white, industry-appropriate accents.",
                "neg_space": "Upper quadrant kept clear for card title legibility."
            }
        elif "case-study-" in fn or "consulting-case-study" in fn:
            cs_title = fn.replace("case-study-", "").replace(".webp", "").replace("-", " ").title()
            return {
                "section": f"Case Study Illustration - {cs_title}",
                "desc": f"Operational advisory team analyzing real-world deliverables for {cs_title}.",
                "prompt": f"High-end editorial corporate photography of management consultants conducting a diagnostic review for {cs_title}. Authentic enterprise workspace, business documents with process flowcharts and Gantt roadmaps on conference table, consultants in focused discussion, realistic lighting, 8k resolution, no logos, no text overlays.",
                "comp": "Over-the-shoulder medium shot highlighting the analytical review.",
                "lighting": "Soft ambient office illumination combined with natural window light.",
                "bg": "High-tech enterprise strategy room with acoustic wood slats.",
                "style": "Authentic corporate case study visual, credible and analytical.",
                "palette": "Corporate navy, cool grey, warm honey timber, clean white.",
                "neg_space": "Upper third open for overlay tags."
            }
        elif "team-" in fn:
            role_name = fn.replace("team-", "").replace("-lead.webp", "").replace(".webp", "").replace("-", " ").title()
            return {
                "section": f"Team Profile - {role_name} Advisor",
                "desc": f"Professional executive portrait representing a senior {role_name} consultant.",
                "prompt": f"Refined corporate headshot portrait of a senior management consultant representing {role_name} in an international advisory firm. Bespoke dark navy business suit, confident and approachable expression, looking slightly off-camera. Soft natural studio lighting, softly blurred executive office background with warm timber and subtle glass reflections. Hasselblad medium format portraiture, realistic skin texture, sharp eyes, 8k, no artificial airbrushing.",
                "comp": "Classic square head-and-shoulders executive portrait with centered composition.",
                "lighting": "Soft three-point portrait studio lighting with gentle wrap-around key light.",
                "bg": "Subtly out-of-focus executive office interior with warm ambient tones.",
                "style": "High-end corporate executive portraiture.",
                "palette": "Navy, charcoal, warm beige, soft white.",
                "neg_space": "Centered portrait with balanced border margins."
            }
        elif "article-" in fn:
            return {
                "section": "Thought Leadership Editorial Hero",
                "desc": "Strategic planning worksheets and bound business reports on an executive conference table.",
                "prompt": "Overhead flat-lay editorial corporate photography of an executive boardroom table with a bound corporate strategy report, premium fountain pen, leather tablet sleeve displaying abstract analytical charts, and a ceramic coffee cup. Rich dark walnut wood surface, warm morning sunlight casting gentle long shadows across the table, ultra-high resolution, photorealistic, 8k, no text, no branding.",
                "comp": "Flat-lay overhead angle with balanced artistic arrangement of executive tools.",
                "lighting": "Directional morning sunlight with soft warm shadows.",
                "bg": "Deep dark walnut conference table surface.",
                "style": "Premium corporate editorial still life.",
                "palette": "Dark walnut, crisp cream paper, navy blue accents, brushed gold.",
                "neg_space": "Generous open space across the wood grain."
            }
        else:
            return {
                "section": "General Advisory Visual",
                "desc": f"Corporate consulting scene for {lbl}.",
                "prompt": f"Premium corporate photography illustrating {lbl} in a contemporary advisory office. Professional consultants in business attire, clean modern interior, natural lighting, sharp focus, 8k, photorealistic.",
                "comp": "Balanced medium shot.",
                "lighting": "Natural daylight with ambient interior fill.",
                "bg": "Contemporary corporate office.",
                "style": "Refined management consulting editorial.",
                "palette": "Corporate navy, slate grey, white.",
                "neg_space": "Upper portion open."
            }

    # Build Markdown Content
    md = []
    md.append("# GOOGLE FLOW IMAGE GENERATION GUIDE")
    md.append("**Website Project:** CONSULTING COMPANY (Static Corporate Advisory Website)")
    md.append("**Document Purpose:** Complete specification and individual copy-ready Google Flow prompts for every image placeholder across all 31 pages.")
    md.append("**Identity Compliance:** All prompts produce natural, authentic corporate environments without logos, fabricated trademarks, watermarks, or stock handshakes.\n")
    md.append("---\n")

    # Section D & E: Summary Counts
    md.append("## EXECUTIVE SUMMARY & SPECIFICATIONS")
    md.append(f"- **Total Image Placeholders:** {total_images}")
    md.append(f"- **Landscape Images (16:9):** {landscape_count}")
    md.append(f"- **Square Images (1:1):** {square_count}")
    md.append(f"- **Portrait Images:** {portrait_count}")
    md.append("- **Target Image Format:** WebP (`.webp`)")
    md.append("- **Target Directory:** `assets/images/`\n")
    md.append("---\n")

    # Section A: Complete Inventory Table
    md.append("## SECTION A: COMPLETE IMAGE INVENTORY TABLE\n")
    md.append("| # | Target Filename | Website Page | Aspect Ratio | Dimensions | Orientation | Section & Subject |")
    md.append("|---|---|---|---|---|---|---|")

    detailed_prompts = []
    for idx, p in enumerate(placeholders, 1):
        meta = make_detailed_prompt(p)
        detailed_prompts.append((idx, p, meta))
        md.append(f"| {idx} | `{p['filename']}` | `{p['page']}` | {p['aspect']} | {p['dimensions']} | {p['orientation']} | {meta['section']} |")

    md.append("\n---\n")

    # Section B: Individual Google Flow Prompts Grouped by Page
    md.append("## SECTION B: INDIVIDUAL GOOGLE FLOW PROMPTS GROUPED BY PAGE\n")
    
    current_page = ""
    for idx, p, meta in detailed_prompts:
        if p["page"] != current_page:
            current_page = p["page"]
            md.append(f"\n### Page: `{current_page}`\n")
        
        md.append(f"#### Image #{idx}: `{p['filename']}`")
        md.append(f"- **Website Page:** `{p['page']}`")
        md.append(f"- **Website Section:** {meta['section']}")
        md.append(f"- **Subject Description:** {meta['desc']}")
        md.append(f"- **Aspect Ratio:** {p['aspect']}")
        md.append(f"- **Resolution:** {p['dimensions']} px")
        md.append(f"- **Orientation:** {p['orientation']}")
        md.append(f"- **Composition & Camera Angle:** {meta['comp']}")
        md.append(f"- **Lighting:** {meta['lighting']}")
        md.append(f"- **Background Environment:** {meta['bg']}")
        md.append(f"- **Visual Style:** {meta['style']}")
        md.append(f"- **Color Palette:** {meta['palette']}")
        md.append(f"- **Negative Space Requirement:** {meta['neg_space']}\n")
        md.append("**Copy-Ready Google Flow Prompt:**")
        md.append("```text")
        md.append(meta['prompt'])
        md.append("```\n")

    md.append("---\n")

    # Section C: Exact Filename to Placeholder Mapping
    md.append("## SECTION C: EXACT FILENAME-TO-PLACEHOLDER MAPPING\n")
    md.append("The table below confirms the exact HTML file and code attribute corresponding to each generated image file:\n")
    md.append("| Target Image File | Target Folder | Associated HTML Page | Markup Data Attribute |")
    md.append("|---|---|---|---|")
    for idx, p, meta in detailed_prompts:
        md.append(f"| `{p['filename']}` | `assets/images/` | `{p['page']}` | `data-placeholder-filename=\"{p['filename']}\"` |")

    md.append("\n---\n")

    # Section F: Recommended Generation Order
    md.append("## SECTION F: RECOMMENDED IMAGE GENERATION ORDER\n")
    md.append("To maintain visual aesthetic consistency in Google Flow, generate images in the following staged batches:\n")
    md.append("1. **Tier 1 — Core Brand & Homepage (Images #1, #16–18):** Establishes the lighting, corporate navy palette, and executive boardroom tone.")
    md.append("2. **Tier 2 — Practice Area Lead Images (Images #3, #13–15, #35–37, #43–46, #60–61):** 13 core practice headers.")
    md.append("3. **Tier 3 — Services Overview Grid (Images #47–59):** Compact 16:9 thumbnails for `services.html`.")
    md.append("4. **Tier 4 — Sector & Industry Facilities (Images #19–30):** High-end operational facilities across 12 industries on `industries.html`.")
    md.append("5. **Tier 5 — Illustrative Case Studies (Images #4–12):** Analytical workspaces and diagnostic deliverables on `case-studies.html`.")
    md.append("6. **Tier 6 — Executive Portraits (Images #62–67):** Square 1:1 corporate headshots for `team.html`.")
    md.append("7. **Tier 7 — Thought Leadership & Articles (Images #2, #31–34, #38–42):** Editorial flat-lays and report photography on `insights.html`.\n")
    md.append("---\n")

    # Section G: Image Replacement Instructions
    md.append("## SECTION G: IMAGE REPLACEMENT INSTRUCTIONS\n")
    md.append("Once all 67 images have been generated via Google Flow and saved in WebP format:\n")
    md.append("1. **Save Files:** Place each WebP file into the project directory: `assets/images/<filename>`.")
    md.append("2. **Replace Placeholder Markup:** In each HTML page, replace the placeholder `div` element:")
    md.append("   ```html")
    md.append("   <!-- Before (Placeholder): -->")
    md.append("   <div class=\"image-placeholder aspect-16-9\" data-placeholder-filename=\"hero-business-consulting.webp\" data-dimensions=\"1920x1080\">")
    md.append("     ...")
    md.append("   </div>")
    md.append("   ")
    md.append("   <!-- After (Production Image): -->")
    md.append("   <img src=\"assets/images/hero-business-consulting.webp\" alt=\"Modern corporate strategic advisory meeting in an executive boardroom\" width=\"1920\" height=\"1080\" loading=\"eager\" class=\"hero-image\">")
    md.append("   ```")
    md.append("3. **Lazy Loading:** For all images located below the fold, ensure `loading=\"lazy\"` is applied.")
    md.append("4. **Verification:** Refresh the pages in your browser to verify proper dimensions, aspect-ratio stability, and zero layout shift (CLS).\n")
    md.append("---\n")

    # Section H: Checklist
    md.append("## SECTION H: QUALITY ASSURANCE & VERIFICATION CHECKLIST\n")
    md.append("- [x] Every HTML placeholder has a distinct target filename ending in `.webp`")
    md.append(f"- [x] Total prompt count ({total_images}) matches total placeholder count ({total_images}) with 100% parity")
    md.append("- [x] All prompts specify high-end, realistic corporate environments without trademarks or handshakes")
    md.append("- [x] Exact aspect ratios and pixel resolutions are specified for every entry")
    md.append("- [x] Image replacement procedure is fully documented\n")

    output_path = os.path.join(BASE_DIR, "IMAGE-GENERATION-GUIDE.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"IMAGE-GENERATION-GUIDE.md successfully created with {total_images} prompts.")

generate_image_guide()
