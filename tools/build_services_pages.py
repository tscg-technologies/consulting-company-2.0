import os
from build_helpers import get_page_shell, make_placeholder
from generate_pages_part1 import register_placeholder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build_about():
    about_img = register_placeholder(
        "about.html",
        "Corporate Philosophy & Principles",
        "about-corporate-philosophy.webp",
        "aspect-16-9",
        "1920x1080",
        "Landscape",
        "Strategic consulting advisory session in a bright corporate architectural boardroom with business consultants discussing strategic plans.",
        "High-angle view of a serene, bright corporate consulting conference space. Three senior business consultants in crisp contemporary professional attire reviewing architectural blueprints and corporate flowcharts on an elongated oak table. Warm ambient natural light streaming through large windows, minimal aesthetic, calm confidence, photorealistic commercial photography.",
        "Wide environmental portrait showing collaborative dynamic and minimalist interior space.",
        "Soft diffused daylight complemented by soft recessed ceiling lighting.",
        "Refined minimalist corporate boardroom with neutral wall panels.",
        "High-end corporate documentary, authentic and editorial.",
        "Slate grey, warm oak, navy accents, pure white.",
        "Open upper area for breathing room."
    )

    body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>About</li>
        </ul>
        <h1 class="page-hero-title">Helping Organizations Navigate Complexity With Clarity</h1>
        <p class="page-hero-desc">We are an independent business consulting firm dedicated to providing clear strategic direction, operational analysis, and structured problem-solving for enterprises across stages.</p>
      </div>
    </section>

    <!-- Mission & Philosophy Section -->
    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Our Philosophy</span>
            <h2 class="section-title">Objective Thinking Grounded in Business Realities</h2>
            <p class="lead">Organizations face an abundance of noise, conflicting priorities, and shifting market conditions. Our purpose is to cut through friction and deliver clarity.</p>
            <p>We believe that sound business strategy does not rely on buzzwords or rigid templates. Sustainable progress requires an honest diagnostic of current capabilities, disciplined prioritization, and pragmatic roadmaps that teams can actually execute.</p>
            <p>Our advisory work is strictly vendor-neutral, practical, and tailored to the unique operational realities of each business engagement.</p>
          </div>
          <div>
            {about_img}
          </div>
        </div>

        <div class="grid-2">
          <div class="card" style="border-top: 3px solid var(--navy-primary);">
            <div class="card-icon" style="background: var(--blue-subtle);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
            </div>
            <h3 class="card-title">Our Mission</h3>
            <p class="card-desc">To empower leadership teams and business owners with actionable insights, structured analysis, and proven frameworks that enable informed decision-making and durable organizational value.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--gold-accent);">
            <div class="card-icon" style="background: var(--gold-light); color: var(--gold-accent);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </div>
            <h3 class="card-title">Our Vision</h3>
            <p class="card-desc">To be the trusted advisory partner of choice for organizations seeking clarity, operational excellence, and disciplined growth without commercial exaggeration.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How We Think & Collaborate -->
    <section class="section bg-light-blue">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Core Principles</span>
          <h2 class="section-title">How We Think and How We Collaborate</h2>
          <p class="section-subtitle">Our consulting engagements are guided by five core operational values.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 style="font-size: 1.2rem; color: var(--navy-primary); margin-bottom: 0.65rem;">1. Diagnostic Rigor</h3>
            <p style="font-size: 0.9rem;">We avoid premature solutions. We examine operating data, interview front-line managers, and test assumptions before formulating recommendations.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; color: var(--navy-primary); margin-bottom: 0.65rem;">2. Transparent Communication</h3>
            <p style="font-size: 0.9rem;">We deliver clear, unvarnished business assessments. If an initiative carries high execution risk or weak return profiles, we highlight it clearly.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; color: var(--navy-primary); margin-bottom: 0.65rem;">3. Practical Deliverables</h3>
            <p style="font-size: 0.9rem;">We design deliverables that can be handed directly to operational managers, complete with owners, timelines, and measurable milestones.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; color: var(--navy-primary); margin-bottom: 0.65rem;">4. Collaborative Alignment</h3>
            <p style="font-size: 0.9rem;">Strategy created in a silo rarely succeeds. We collaborate closely with internal stakeholders to build organizational buy-in from day one.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; color: var(--navy-primary); margin-bottom: 0.65rem;">5. Long-Term Value Focus</h3>
            <p style="font-size: 0.9rem;">We reject short-term gimmicks in favor of structural improvements that build enduring competitive advantages and operational resilience.</p>
          </div>
          <div class="card">
            <h3 style="font-size: 1.2rem; color: var(--navy-primary); margin-bottom: 0.65rem;">6. Confidentiality & Integrity</h3>
            <p style="font-size: 0.9rem;">We hold client business discussions, financial analyses, and competitive strategies under strict non-disclosure and professional standards.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Consultation CTA -->
    <section class="section bg-white" style="border-top: 1px solid var(--border-color);">
      <div class="container container-narrow text-center">
        <h2 class="section-title">Discuss Your Organizational Priorities</h2>
        <p class="section-subtitle" style="margin-bottom: 2rem;">Every business engagement begins with an open, structured discovery conversation.</p>
        <a href="book-consultation.html" class="btn btn-primary btn-lg">Book an Exploratory Discussion</a>
      </div>
    </section>
    '''

    html = get_page_shell(
        "About the Firm | Helping Organizations Navigate Complexity With Clarity",
        "Learn about our consulting philosophy, advisory values, problem-solving approach, and commitment to clear, business-focused decision making.",
        "about.html",
        "about",
        body
    )
    with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Page 2: about.html written.")


def build_services_overview():
    services_list = [
        ("Business Consulting", "business-consulting.html", "Strategic business planning, model evaluation, and market opportunity assessments to drive business sustainability.", "Unclear business models, stagnant sales channels, and operational bottlenecks.", "Comprehensive business review report, growth roadmap, and implementation priority plan.", "service-business-consulting.webp"),
        ("Management Consulting", "management-consulting.html", "Organizational structure optimization, decision frameworks, and leadership alignment to improve organizational execution.", "Siloed management teams, unclear reporting lines, and slow decision-making cycles.", "Governance framework, leadership accountability matrix (RACI), and management review cadence.", "service-management-consulting.webp"),
        ("Strategy Consulting", "strategy-consulting.html", "Corporate strategy, competitive positioning, and expansion feasibility studies for long-term market differentiation.", "Evolving industry dynamics, competitive erosion, and unfocused product portfolios.", "Multi-year strategic roadmap, competitive landscape matrix, and market entry strategy.", "service-strategy-consulting.webp"),
        ("Financial Consulting", "financial-consulting.html", "Budget planning, cost structure rationalization, and cash flow forecasting to enhance commercial visibility.", "Opaque overhead costs, cash flow unpredictability, and misaligned unit economics.", "Financial performance diagnostic, working capital plan, and scenario planning models.", "service-financial-consulting.webp"),
        ("HR Consulting", "hr-consulting.html", "Workforce planning, performance management architecture, and talent retention strategies.", "High employee turnover, fragmented recruitment processes, and uncalibrated performance reviews.", "Talent management roadmap, competency framework, and workforce restructuring guide.", "service-hr-consulting.webp"),
        ("Marketing Consulting", "marketing-consulting.html", "Customer segmentation, brand value proposition, and customer acquisition funnel planning.", "High customer acquisition costs, inconsistent messaging, and unmeasured marketing channels.", "Marketing funnel blueprint, audience segmentation playbook, and measurement framework.", "service-marketing-consulting.webp"),
        ("IT Consulting", "it-consulting.html", "Technology stack assessment, vendor evaluation, enterprise architecture, and IT project advisory.", "Legacy system debt, disconnected software tools, and uncontrolled IT spending.", "IT infrastructure assessment, vendor evaluation matrix, and systems modernization plan.", "service-it-consulting.webp"),
        ("Digital Transformation", "digital-transformation.html", "Process digitization, cloud migration planning, and digital workflow automation for modern enterprises.", "Manual paper-based operations, poor data accessibility, and fragmented customer touchpoints.", "Digital readiness assessment, phased transformation roadmap, and change enablement guide.", "service-digital-transformation.webp"),
        ("Operations Consulting", "operations-consulting.html", "Process engineering, bottleneck elimination, supply chain analysis, and operational cost reduction.", "Production delays, excess inventory, supply chain friction, and quality variances.", "Process flow redesign, Lean operating principles, and standard operating procedures (SOPs).", "service-operations-consulting.webp"),
        ("Startup Consulting", "startup-consulting.html", "Foundational business model validation, MVP scoping, and go-to-market design for early-stage ventures.", "Unvalidated market hypotheses, premature scaling, and capital allocation confusion.", "Startup operational roadmap, unit economics model, and investor pitch deck readiness brief.", "service-startup-consulting.webp"),
        ("Risk Management", "risk-management.html", "Operational risk mapping, business continuity planning, and internal compliance review frameworks.", "Unidentified single points of failure, supply disruptions, and regulatory compliance gaps.", "Enterprise risk matrix, business continuity plan (BCP), and mitigation action register.", "service-risk-management.webp"),
        ("Project Management", "project-management.html", "Project governance, PMO setup, resource scheduling, and delivery risk oversight.", "Delayed project milestones, scope creep, budget overruns, and weak delivery governance.", "PMO charter, milestone tracking framework, and project steering dashboard template.", "service-project-management.webp"),
        ("Organizational Development", "organizational-development.html", "Cultural transformation, change management, and leadership development programs.", "Resistance to strategic change, team burnout, and low employee engagement during restructuring.", "Change enablement roadmap, culture assessment report, and leadership alignment workshop.", "service-org-development.webp"),
    ]

    cards_html = []
    for title, url, desc, challenges, deliverables, img_file in services_list:
        p_img = register_placeholder(
            "services.html",
            f"Service Card - {title}",
            img_file,
            "aspect-16-9",
            "640x360",
            "Landscape",
            f"Professional consulting engagement visual illustrating {title} with consultants collaborating in a corporate setting.",
            f"Professional corporate consulting setting representing {title}. Business advisors reviewing strategic documents, analytical charts, and architectural diagrams. Clean corporate boardroom setting, focused expressions, modern corporate navy and white environment, sharp focus, natural light, premium corporate photography.",
            "Balanced medium shot with consultants working over corporate documentation.",
            "Clear natural daylight with subtle interior architectural lighting.",
            "Contemporary corporate conference suite with glass partitions.",
            "High-end corporate commercial style, crisp and elegant.",
            "Navy blue, light slate, warm timber, clean white.",
            "Balanced composition with clear focal subject."
        )

        card = f'''
        <div class="service-feature-card hover-lift">
          <div style="margin-bottom: 1.25rem;">
            {p_img}
          </div>
          <h3 style="font-size: 1.35rem; color: var(--navy-primary); margin-bottom: 0.65rem;">{title}</h3>
          <p style="font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 1.25rem;">{desc}</p>
          
          <div style="background: var(--blue-subtle); padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1rem;">
            <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--navy-primary); margin-bottom: 0.35rem;">Typical Business Challenges</div>
            <div style="font-size: 0.85rem; color: var(--text-secondary);">{challenges}</div>
          </div>

          <div style="background: var(--warm-white); padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); margin-bottom: 1.5rem;">
            <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--gold-accent); margin-bottom: 0.35rem;">Consulting Deliverables</div>
            <div style="font-size: 0.85rem; color: var(--text-main); font-weight: 500;">{deliverables}</div>
          </div>

          <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; padding-top: 1rem; border-top: 1px solid var(--border-light);">
            <a href="{url}" class="btn btn-secondary btn-sm">Learn More &rarr;</a>
            <a href="book-consultation.html" class="btn btn-primary btn-sm">Book Consultation</a>
          </div>
        </div>
        '''
        cards_html.append(card)

    cards_joined = "\n".join(cards_html)

    body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Services</li>
        </ul>
        <h1 class="page-hero-title">Consulting Solutions Designed Around Business Challenges</h1>
        <p class="page-hero-desc">Explore our full suite of 13 structured consulting practices. Each engagement provides structured diagnostics, pragmatic solutions, and clear execution roadmaps.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2">
{cards_joined}
        </div>
      </div>
    </section>

    <section class="section bg-light-blue text-center">
      <div class="container container-narrow">
        <h2 class="section-title">Require a Tailored Advisory Scope?</h2>
        <p class="section-subtitle" style="margin-bottom: 2rem;">Many client challenges span multiple disciplines—such as simultaneous operational and digital restructuring. We configure cross-functional engagements aligned with your exact needs.</p>
        <a href="book-consultation.html" class="btn btn-primary btn-lg">Request a Custom Engagement Discussion</a>
      </div>
    </section>
    '''

    html = get_page_shell(
        "Consulting Services Overview | 13 Enterprise Advisory Practices",
        "Comprehensive consulting services covering business planning, management, corporate strategy, finance, HR, technology, operations, and organizational development.",
        "services.html",
        "services",
        body
    )
    with open(os.path.join(BASE_DIR, "services.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Page 3: services.html written.")

build_about()
build_services_overview()
