import os
from build_helpers import get_page_shell, make_placeholder
from generate_pages_part1 import register_placeholder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_corp_pages():
    # ====================================================
    # 17. industries.html
    # ====================================================
    industries_data = [
        ("Manufacturing", "Process bottlenecks, equipment downtime, supply chain vulnerabilities, and quality variance.", "Operations Consulting, Risk Management, Digital Transformation", "Lean production line optimization and automated inventory tracking.", "industry-manufacturing.webp"),
        ("Healthcare", "Administrative overhead, regulatory record-keeping complexity, patient flow delays, and staff burnout.", "Management Consulting, HR Consulting, Operations Consulting", "Patient journey mapping, departmental staffing models, and compliance workflows.", "industry-healthcare.webp"),
        ("Education", "Enrollment forecasting fluctuations, legacy administrative software, and faculty workload allocation.", "Organizational Development, IT Consulting, Strategy Consulting", "Digital student lifecycle management and institutional strategic planning.", "industry-education.webp"),
        ("Real Estate", "Capital allocation uncertainty, multi-asset portfolio visibility, and property management operational friction.", "Financial Consulting, Business Consulting, Strategy Consulting", "Asset cash flow modeling and tenant management workflow standardization.", "industry-real-estate.webp"),
        ("Retail", "Omnichannel inventory misalignment, seasonal demand unpredictability, and margin erosion from returns.", "Operations Consulting, Marketing Consulting, Strategy Consulting", "Unified inventory visibility, customer retention funnels, and store labor sizing.", "industry-retail.webp"),
        ("E-commerce", "High customer acquisition costs (CAC), cart abandonment, fulfillment delays, and platform scalability.", "Marketing Consulting, IT Consulting, Operations Consulting", "Conversion funnel optimization, warehouse dispatch workflows, and unit economics modeling.", "industry-ecommerce.webp"),
        ("Technology", "Rapid team scaling friction, technical debt accumulation, product-market positioning, and churn management.", "Strategy Consulting, Management Consulting, HR Consulting", "Organizational spans of control, SaaS metric frameworks, and executive governance.", "industry-technology.webp"),
        ("Financial Services", "Legacy core banking interfaces, operational risk exposure, reporting compliance, and customer digital onboarding.", "Risk Management, IT Consulting, Digital Transformation", "Digital onboarding journey redesign, operational risk matrices, and vendor selection.", "industry-financial-services.webp"),
        ("Hospitality", "Labor turnover, seasonal cash flow swings, food cost variances, and online brand reputation management.", "HR Consulting, Financial Consulting, Operations Consulting", "Shift scheduling optimization, culinary waste audits, and guest feedback loops.", "industry-hospitality.webp"),
        ("Logistics & Supply Chain", "Fleet idle time, cross-docking delays, route fuel inefficiency, and freight partner tracking friction.", "Operations Consulting, Risk Management, Digital Transformation", "Dynamic dispatch routing models, carrier SLA monitoring, and warehouse throughput audits.", "industry-logistics.webp"),
        ("Professional Services", "Billable utilization variance, partner compensation structures, knowledge silos, and project margin erosion.", "Business Consulting, Management Consulting, Project Management", "Utilization KPI scorecards, project delivery governance, and client onboarding workflows.", "industry-professional-services.webp"),
        ("Startups & Scaleups", "Premature cash burn, unvalidated go-to-market channels, leadership role confusion, and fundraising readiness.", "Startup Consulting, Strategy Consulting, Financial Consulting", "Unit economics stress testing, MVP prioritization matrices, and investor pitch documentation.", "industry-startups.webp")
    ]

    ind_cards_html = []
    for name, challenges, services, focus, img_file in industries_data:
        p_img = register_placeholder(
            "industries.html",
            f"Industry Card - {name}",
            img_file,
            "aspect-16-9",
            "600x338",
            "Landscape",
            f"Commercial enterprise environment representing the {name} sector with modern operational facilities.",
            f"Authentic modern commercial setting representing {name}. Crisp, clean, sophisticated business environment, focused professionals at work, natural lighting, contemporary architecture, ultra-realistic commercial photography.",
            "Medium shot capturing the authentic operational setting of the industry.",
            "Balanced natural daylight with soft fill.",
            f"Clean modern architectural facility suited for {name}.",
            "Premium corporate editorial photography.",
            "Navy, charcoal grey, cool steel, white.",
            "Clear upper area."
        )

        ind_cards_html.append(f'''
        <div class="card hover-lift">
          <div style="margin-bottom: 1.25rem;">{p_img}</div>
          <h3 style="font-size: 1.3rem; color: var(--navy-primary); margin-bottom: 0.65rem;">{name}</h3>
          
          <div style="background: var(--blue-subtle); padding: 0.85rem; border-radius: var(--radius-sm); margin-bottom: 0.75rem;">
            <div style="font-size: 0.72rem; text-transform: uppercase; font-weight: 700; color: var(--navy-primary); margin-bottom: 0.25rem;">Common Sector Challenges</div>
            <div style="font-size: 0.82rem; color: var(--text-secondary);">{challenges}</div>
          </div>

          <div style="background: var(--warm-white); padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid var(--border-light); margin-bottom: 0.75rem;">
            <div style="font-size: 0.72rem; text-transform: uppercase; font-weight: 700; color: var(--blue-accent); margin-bottom: 0.25rem;">Relevant Consulting Practices</div>
            <div style="font-size: 0.82rem; color: var(--text-main); font-weight: 500;">{services}</div>
          </div>

          <div style="margin-bottom: 1.25rem;">
            <div style="font-size: 0.72rem; text-transform: uppercase; font-weight: 700; color: var(--gold-accent); margin-bottom: 0.25rem;">Potential Consulting Focus</div>
            <div style="font-size: 0.85rem; color: var(--text-secondary);">{focus}</div>
          </div>

          <div style="margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
            <span class="demo-pill" style="font-size: 0.68rem;">Cross-Functional</span>
            <a href="book-consultation.html" class="btn btn-secondary btn-sm">Consult on {name} &rarr;</a>
          </div>
        </div>
        ''')

    ind_cards_joined = "\n".join(ind_cards_html)

    ind_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Industries</li>
        </ul>
        <h1 class="page-hero-title">Sector-Focused Consulting Solutions</h1>
        <p class="page-hero-desc">We tailor our strategic frameworks, operational methodologies, and diagnostic tools to the specific market dynamics and regulatory environments of 12 distinct industries.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Sector Expertise Disclaimer -->
        <div class="notice-box notice-info" style="margin-bottom: 3rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Demonstration Notice:</strong> The sector sections below illustrate our multi-disciplinary consulting capabilities applied to generic business models across industries. They do not claim active commercial contracts, certified trade licenses, or proprietary sector accreditation with specific regulatory authorities.
          </div>
        </div>

        <div class="grid-3">
{ind_cards_joined}
        </div>
      </div>
    </section>

    <section class="section bg-light-blue text-center">
      <div class="container container-narrow">
        <h2 class="section-title">Operating in a Specialized or Niche Sector?</h2>
        <p class="section-subtitle" style="margin-bottom: 2rem;">Our consulting frameworks are rooted in foundational operational disciplines—process analysis, unit economics, and organizational design—which translate effectively across specialized domains.</p>
        <a href="book-consultation.html" class="btn btn-primary btn-lg">Discuss Your Industry Challenges</a>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "industries.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Industries Served | 12 Enterprise Sector Practices",
            "Consulting capabilities across manufacturing, healthcare, technology, retail, financial services, education, real estate, logistics, and professional services.",
            "industries.html",
            "industries",
            ind_body
        ))
    print("Page 17: industries.html written.")

    # ====================================================
    # 18. methodology.html
    # ====================================================
    img_meth = register_placeholder(
        "methodology.html",
        "Methodology Hero",
        "consulting-methodology-execution.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Consulting engagement lead mapping the five-stage advisory process across discovery, analysis, and implementation on a glass planning surface.",
        "Senior business advisory director presenting the five stages of consulting methodology to corporate directors in a brightly illuminated architectural glass suite. Professional demeanor, clean lines, contemporary boardroom setting, crisp corporate photography.",
        "Medium-wide shot with clear depth of field and diagram focus.",
        "Balanced natural daylight through panoramic windows.",
        "Contemporary corporate glass suite.",
        "Refined editorial commercial photography.",
        "Corporate navy, gold accents, crisp white.",
        "Open upper third."
    )

    meth_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Our Approach</li>
        </ul>
        <h1 class="page-hero-title">A Structured Approach to Solving Complex Business Problems</h1>
        <p class="page-hero-desc">We apply a rigorous five-stage consulting framework designed to maintain analytical rigor, transparent communication, and grounded implementation support.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Methodology Disclaimer -->
        <div class="notice-box" style="margin-bottom: 3.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Advisory Framework Clarification:</strong> The consulting lifecycle detailed below outlines our standard professional service approach. It represents sound business analysis practices rather than a certified proprietary algorithm or trademarked academic framework.
          </div>
        </div>

        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Disciplined Execution</span>
            <h2 class="section-title">The Five Stages of a Consulting Engagement</h2>
            <p class="lead">Effective consulting avoids jumping to hasty conclusions. By dividing engagements into clear, chronological gates, we ensure thorough stakeholder alignment and grounded recommendations.</p>
            <p>Each stage concludes with explicit decision checkpoints, ensuring client leadership maintains full visibility and control throughout the engagement lifecycle.</p>
          </div>
          <div>{img_meth}</div>
        </div>

        <!-- Five Stages Detailed Breakdown -->
        <div class="accordion" style="margin-bottom: 3.5rem;">
          <div class="accordion-item active">
            <button class="accordion-header" aria-expanded="true">
              <span><strong>Stage 01 — Discover:</strong> Understand the Business, Stakeholders, and Objectives</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>The engagement initiates with comprehensive orientation sessions. We interview executive sponsors, operational department heads, and key staff members to understand the commercial context, strategic intent, and observed pain points.</p>
              <div style="background: var(--blue-subtle); padding: 1rem; border-radius: var(--radius-sm);">
                <strong>Key Deliverables:</strong> Engagement Charter, Stakeholder Map, Information Request Checklist, and Scope Baseline Document.
              </div>
            </div>
          </div>

          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span><strong>Stage 02 — Assess:</strong> Review Current Processes, Systems, and Baseline Data</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Our consultants review existing documentation, financial reports, operational workflows, and technology architectures. We observe day-to-day operations and collect quantitative baseline data to map current-state performance.</p>
              <div style="background: var(--blue-subtle); padding: 1rem; border-radius: var(--radius-sm);">
                <strong>Key Deliverables:</strong> Current-State Process Maps, Baseline KPI Scorecards, and Operational Bottleneck Inventory.
              </div>
            </div>
          </div>

          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span><strong>Stage 03 — Analyze:</strong> Identify Root Causes and Model Strategic Alternatives</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>We synthesize findings to distinguish surface symptoms from core structural constraints. We test hypotheses, benchmark peer operations, model financial trade-offs, and assess risk profiles across multiple intervention options.</p>
              <div style="background: var(--blue-subtle); padding: 1rem; border-radius: var(--radius-sm);">
                <strong>Key Deliverables:</strong> Root Cause Diagnostic Brief, Scenario Comparison Models, and Trade-Off Assessment Matrix.
              </div>
            </div>
          </div>

          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span><strong>Stage 04 — Recommend:</strong> Present Actionable Solutions and Phased Roadmaps</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>We formulate practical, prioritized solutions accompanied by structured implementation plans. Every recommendation is paired with resource estimates, milestone timelines, risk mitigations, and expected operational outcomes.</p>
              <div style="background: var(--blue-subtle); padding: 1rem; border-radius: var(--radius-sm);">
                <strong>Key Deliverables:</strong> Final Consulting Report, Target Operating Model (TOM), and Phased Implementation Roadmap.
              </div>
            </div>
          </div>

          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span><strong>Stage 05 — Support:</strong> Implementation Governance and Progress Reviews</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Where included in the engagement scope, we support internal project teams during early implementation phases, facilitate steering committee reviews, and assist in calibrating workflows to ensure lasting adoption.</p>
              <div style="background: var(--blue-subtle); padding: 1rem; border-radius: var(--radius-sm);">
                <strong>Key Deliverables:</strong> Steering Committee Cadence, Milestone Burn-Down Reports, and Post-Engagement Calibration Review.
              </div>
            </div>
          </div>
        </div>

        <div style="text-align: center;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Schedule an Initial Discovery Discussion</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "methodology.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Our Consulting Approach | Structured Five-Stage Methodology",
            "A structured five-stage consulting framework: Discover, Assess, Analyze, Recommend, and Support. Disciplined problem-solving for enterprise challenges.",
            "methodology.html",
            "methodology",
            meth_body
        ))
    print("Page 18: methodology.html written.")

    # ====================================================
    # 19. case-studies.html
    # ====================================================
    case_studies_list = [
        ("Business Growth Planning Demo", "business-strategy", "Retail & Consumer", "Addressing multi-channel margin erosion and formulating an omnichannel expansion roadmap.", "case-study-cs1.webp"),
        ("Operational Process Review Demo", "operations", "Industrial Manufacturing", "Streamlining warehouse dispatch workflows, reducing batch rework, and establishing standard operating procedures.", "case-study-cs2.webp"),
        ("Digital Transformation Planning Demo", "digital-transformation", "Enterprise Logistics", "Migrating manual dispatch manifests to a centralized cloud TMS with real-time tracking.", "case-study-cs3.webp"),
        ("Financial Performance Analysis Demo", "financial-planning", "Commercial Distribution", "Segmenting gross margin contribution by SKU and rationalizing working capital cycles.", "case-study-cs4.webp"),
        ("Workforce Planning Demo", "hr-workforce", "Technology Services", "Designing job grading architecture and objective quarterly performance calibration rubrics.", "case-study-cs5.webp"),
        ("Startup Business Strategy Demo", "startup-strategy", "B2B SaaS Venture", "Pressure-testing customer acquisition costs, validating enterprise sales funnels, and building unit economics models.", "case-study-cs6.webp"),
        ("Marketing Funnel Optimization Demo", "marketing-strategy", "Professional Education", "Restructuring high-intent digital conversion funnels and implementing lead attribution scorecards.", "case-study-cs7.webp"),
        ("PMO Delivery Governance Demo", "project-management", "Healthcare Systems", "Setting up steering governance, tracking critical-path milestones, and managing software rollout risks.", "case-study-cs8.webp"),
    ]

    cs_cards_html = []
    for title, cat, ind, desc, img_file in case_studies_list:
        p_img = register_placeholder(
            "case-studies.html",
            f"Case Study - {title}",
            img_file,
            "aspect-16-9",
            "800x450",
            "Landscape",
            f"Advisory team analyzing illustrative operational case study for {title} in a corporate environment.",
            f"Corporate consulting team reviewing illustrative operational case study documentation for {title} in a high-rise office. High detail, authentic business setting, crisp lighting, photorealistic commercial photography.",
            "Medium shot with focus on consulting deliverables and team discussion.",
            "Natural daylight with subtle interior warmth.",
            "Modern corporate conference facility.",
            "Clean editorial business photography.",
            "Navy, slate blue, neutral grey, white.",
            "Top framing open."
        )

        cs_cards_html.append(f'''
        <div class="card hover-lift filterable-item" data-category="{cat}">
          <div style="margin-bottom: 1.25rem;">{p_img}</div>
          <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem; flex-wrap: wrap;">
            <span class="demo-pill" style="font-size: 0.7rem;">{ind}</span>
            <span class="demo-disclaimer-tag">Illustrative Demo Case Study</span>
          </div>
          <h3 class="card-title">{title}</h3>
          <p class="card-desc">{desc}</p>
          <div class="card-footer">
            <a href="case-study-details.html" style="font-weight: 600;">View Case Study Breakdown &rarr;</a>
            <span style="font-size: 0.8rem; color: var(--text-muted);">Demonstration</span>
          </div>
        </div>
        ''')

    cs_cards_joined = "\n".join(cs_cards_html)

    cs_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Case Studies</li>
        </ul>
        <h1 class="page-hero-title">Illustrative Consulting Case Studies</h1>
        <p class="page-hero-desc">Explore demonstration case studies illustrating how our diagnostic frameworks and advisory roadmaps address enterprise challenges across industries.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Prominent Authenticity Disclaimer -->
        <div class="notice-box notice-info" style="margin-bottom: 2.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Mandatory Demo Disclosure:</strong> Every case study presented on this page is an <em>illustrative demonstration scenario</em> designed to demonstrate our consulting approach, analytical rigor, and deliverable structures. In accordance with professional integrity standards, we do not fabricate client identities, publish confidential client data, or invent commercial growth figures.
          </div>
        </div>

        <!-- Filter Controls -->
        <div class="filter-bar">
          <button class="filter-btn active" data-filter="all">All Practice Areas</button>
          <button class="filter-btn" data-filter="business-strategy">Business Strategy</button>
          <button class="filter-btn" data-filter="operations">Operations</button>
          <button class="filter-btn" data-filter="digital-transformation">Digital Transformation</button>
          <button class="filter-btn" data-filter="financial-planning">Financial Planning</button>
          <button class="filter-btn" data-filter="hr-workforce">HR & Workforce</button>
          <button class="filter-btn" data-filter="startup-strategy">Startup Strategy</button>
          <button class="filter-btn" data-filter="marketing-strategy">Marketing Strategy</button>
          <button class="filter-btn" data-filter="project-management">Project Management</button>
        </div>

        <div class="grid-2">
{cs_cards_joined}
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "case-studies.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Illustrative Case Studies | Demonstration Advisory Engagements",
            "Illustrative consulting case studies showcasing strategic frameworks, operational reviews, digital transformation roadmaps, and workforce planning.",
            "case-studies.html",
            "case-studies",
            cs_body
        ))
    print("Page 19: case-studies.html written.")

    # ====================================================
    # 20. case-study-details.html
    # ====================================================
    img_csd = register_placeholder(
        "case-study-details.html",
        "Case Study Detail Hero",
        "consulting-case-study-workspace.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Consultants collaborating over operational workflow redesign maps and Gantt project schedules in an executive project room.",
        "Detailed view of a consulting workspace with enterprise workflow diagrams, milestone execution roadmaps, and analytical notebooks on a conference table. Senior consultant pointing to a critical path node. Professional, realistic corporate photography.",
        "Over-the-shoulder medium shot showing roadmap documents.",
        "Warm directional daylight with clean ambient fill.",
        "Modern enterprise conference room.",
        "Authentic corporate documentary style.",
        "Navy, slate grey, warm timber, clean white.",
        "Upper framing open."
    )

    csd_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="case-studies.html">Case Studies</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Case Study Details</li>
        </ul>
        <div style="margin-bottom: 0.75rem;">
          <span class="demo-disclaimer-tag">Illustrative Demo Case Study — Not an Actual Client Engagement</span>
        </div>
        <h1 class="page-hero-title">Operational Process Review & Capacity Planning Demo</h1>
        <p class="page-hero-desc">An educational case study walkthrough demonstrating multi-plant bottleneck diagnostics, standard operating procedure design, and inventory buffer rationalization.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 3.5rem;">
          <div>
            <span class="eyebrow">Engagement Overview</span>
            <h2 class="section-title">The Business Context</h2>
            <p class="lead">A mid-sized regional manufacturing enterprise operating across three production facilities experienced compounding shipment delays and inventory stockouts during seasonal peak demand.</p>
            <p>Our consulting engagement was chartered to evaluate end-to-end material flow, determine capacity constraints, eliminate redundant managerial sign-offs, and establish a repeatable operational cadence.</p>
          </div>
          <div>{img_csd}</div>
        </div>

        <div class="grid-3" style="margin-bottom: 3.5rem;">
          <div class="card" style="border-top: 3px solid var(--navy-primary);">
            <div class="eyebrow">Industry Context</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Industrial Manufacturing</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary);">Multi-facility production environment handling serialized component assembly and regional distribution.</p>
          </div>
          <div class="card" style="border-top: 3px solid var(--blue-accent);">
            <div class="eyebrow">Engagement Duration</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">12-Week Diagnostic & Design</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary);">4 weeks discovery and baseline assessment, 4 weeks diagnostic analysis, 4 weeks roadmap formulation.</p>
          </div>
          <div class="card" style="border-top: 3px solid var(--gold-accent);">
            <div class="eyebrow">Scope of Deliverables</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Core Operational Artifacts</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary);">Process flow re-engineering blueprint, Lean SOP manual, and central production scheduling dashboard template.</p>
          </div>
        </div>

        <!-- Problem, Assessment, Analysis, Recommendation -->
        <div style="max-width: 900px; margin: 0 auto 4rem;">
          <h2 style="font-size: 1.85rem; margin-bottom: 1rem; color: var(--navy-primary);">The Underlying Operational Challenge</h2>
          <p>Initial interviews with plant supervisors suggested equipment capacity was the primary constraint. However, empirical throughput logs revealed that assembly lines were frequently idle while waiting for paper-based quality sign-offs and component batch transfers between adjacent production cells.</p>

          <h2 style="font-size: 1.85rem; margin: 2rem 0 1rem; color: var(--navy-primary);">Assessment Approach & Analytical Diagnostics</h2>
          <p>Our team conducted physical time-and-motion studies across 14 workstations, mapped 28 distinct handoff gates, and reviewed 6 months of historical shift output logs. We discovered:</p>
          <ul style="padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <li>Work-in-progress (WIP) inventory was accumulating at intermediate testing stations due to batch processing rather than single-piece continuous flow.</li>
            <li>Plant supervisors spent over 35% of their daily shift reconciling physical job tickets with the ERP database manually.</li>
            <li>Safety stock formulas failed to account for supplier lead time standard deviations, leading to recurring stockouts of low-cost consumable fasteners.</li>
          </ul>

          <h2 style="font-size: 1.85rem; margin: 2rem 0 1rem; color: var(--navy-primary);">Strategic Recommendations</h2>
          <p>We designed a three-pronged operational remediation plan:</p>
          <ol style="padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <li><strong>Line Balancing & Cell Reconfiguration:</strong> Re-sequenced assembly tasks to equalize cycle times across workstations, reducing intermediate queueing.</li>
            <li><strong>Digital Quality Verification:</strong> Replaced paper batch tickets with barcoded mobile scan terminals, automating ERP inventory updates at the workstation.</li>
            <li><strong>Dynamic Reorder Point Logic:</strong> Updated inventory parameters using lead time variance distributions rather than static monthly averages.</li>
          </ol>

          <h2 style="font-size: 1.85rem; margin: 2rem 0 1rem; color: var(--navy-primary);">Illustrative Implementation Roadmap</h2>
          <div class="process-timeline" style="grid-template-columns: repeat(3, 1fr); margin-top: 1.5rem; margin-bottom: 2.5rem;">
            <div class="process-card">
              <span class="process-step-num">Weeks 1–4</span>
              <h4 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--navy-primary);">Pilot Cell Rollout</h4>
              <p style="font-size: 0.85rem; color: var(--text-secondary);">Testing re-sequenced workstations on primary line and training shift leaders on new SOPs.</p>
            </div>
            <div class="process-card">
              <span class="process-step-num">Weeks 5–8</span>
              <h4 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--navy-primary);">Digital Terminal Deployment</h4>
              <p style="font-size: 0.85rem; color: var(--text-secondary);">Configuring barcode scanners and decommissioning legacy paper shift handoff sheets.</p>
            </div>
            <div class="process-card">
              <span class="process-step-num">Weeks 9–12</span>
              <h4 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--navy-primary);">Facility-Wide Standardization</h4>
              <p style="font-size: 0.85rem; color: var(--text-secondary);">Extending protocols across secondary plants and embedding monthly operating reviews (MORs).</p>
            </div>
          </div>

          <div style="background: var(--warm-white); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.5rem;">
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Key Takeaway for Leadership Teams</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">Complex operational delays are often caused by administrative friction and uncoordinated handoffs rather than capital equipment shortfalls. Rigorous baseline diagnostics prevent expensive, unnecessary machinery acquisitions.</p>
          </div>
        </div>

        <div style="text-align: center; border-top: 1px solid var(--border-color); padding-top: 3rem;">
          <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Facing Similar Operational Bottlenecks?</h3>
          <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">Discuss your operational workflows with our senior consulting advisors.</p>
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Schedule an Operational Consultation</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "case-study-details.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Case Study Details | Operational Process Review Demo",
            "Detailed demonstration case study examining operational bottleneck analysis, process re-engineering, and implementation roadmaps.",
            "case-study-details.html",
            "case-studies",
            csd_body
        ))
    print("Page 20: case-study-details.html written.")

    # ====================================================
    # 21. team.html
    # ====================================================
    team_roles = [
        ("Principal Strategy Advisor", "Strategy & Corporate Planning", "Focuses on corporate growth roadmaps, market expansion analysis, competitive positioning, and commercial model stress testing.", "team-strategy-lead.webp"),
        ("Director of Operations Advisory", "Operations & Supply Chain", "Specializes in manufacturing throughput analysis, Lean workflow optimization, distribution network design, and quality SOPs.", "team-operations-lead.webp"),
        ("Financial Advisory Consultant", "Financial Modeling & Commercial Analysis", "Conducts financial diagnostics, budgeting frameworks, cash flow planning, cost rationalization, and capital allocation models.", "team-finance-lead.webp"),
        ("Technology Systems Architect", "IT Consulting & Digital Transformation", "Guides enterprise software evaluations, ERP/CRM architecture, cloud adoption planning, and digital workflow automation.", "team-tech-lead.webp"),
        ("Human Resources Advisory Lead", "HR Strategy & Workforce Planning", "Advises on organizational structure, workforce capacity models, competency frameworks, and performance appraisal systems.", "team-hr-lead.webp"),
        ("Organizational Development Specialist", "Change Enablement & Leadership", "Facilitates leadership alignment offsites, cultural diagnostic assessments, and cross-functional change management programs.", "team-od-lead.webp")
    ]

    team_cards_html = []
    for role, practice, desc, img_file in team_roles:
        p_img = register_placeholder(
            "team.html",
            f"Team Profile - {role}",
            img_file,
            "aspect-1-1",
            "400x400",
            "Square",
            f"Abstract professional corporate advisor portrait representing {role} in an executive office setting.",
            f"Professional corporate portrait of a business consulting advisor in tailored formal corporate attire, positioned in a clean contemporary boardroom setting. Subtle architectural depth of field, natural soft lighting, professional and approachable expression, photorealistic commercial photography.",
            "Classic executive headshot framing from shoulders up.",
            "Soft directional window lighting with subtle studio fill.",
            "Subtly blurred contemporary corporate interior with warm timber tones.",
            "Refined corporate editorial portraiture.",
            "Navy, charcoal grey, warm beige, soft white.",
            "Balanced composition with centered subject."
        )

        team_cards_html.append(f'''
        <div class="card hover-lift" style="text-align: center; align-items: center;">
          <div style="width: 140px; height: 140px; border-radius: 50%; overflow: hidden; margin-bottom: 1.25rem; border: 2px solid var(--border-color);">
            {p_img}
          </div>
          <span class="demo-disclaimer-tag" style="margin-bottom: 0.5rem;">Demo Profile</span>
          <h3 style="font-size: 1.25rem; color: var(--navy-primary); margin-bottom: 0.25rem;">{role}</h3>
          <div style="font-size: 0.8125rem; font-weight: 600; color: var(--blue-accent); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">{practice}</div>
          <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.25rem;">{desc}</p>
          <div style="margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border-light); width: 100%;">
            <a href="book-consultation.html" class="btn btn-secondary btn-sm" style="width: 100%;">Consult With Practice &rarr;</a>
          </div>
        </div>
        ''')

    team_cards_joined = "\n".join(team_cards_html)

    team_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Consulting Team</li>
        </ul>
        <h1 class="page-hero-title">Practice Leaders and Advisory Expertise</h1>
        <p class="page-hero-desc">Our multidisciplinary consulting team brings focused analytical capability across strategy, finance, operations, technology, and organizational development.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Identity Rule Compliance Notice -->
        <div class="notice-box" style="margin-bottom: 3.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Demonstration Identity Notice:</strong> In strict compliance with professional identity and privacy guidelines, the profiles displayed below represent generic functional roles and illustrative practice domains. We do not fabricate individual employee names, portraits, academic credentials, prior corporate employers, or commercial resumes. Real practice CVs and credentials are provided under non-disclosure during genuine commercial proposals.
          </div>
        </div>

        <div class="grid-3">
{team_cards_joined}
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "team.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Consulting Team | Practice Roles & Advisory Expertise",
            "Meet our advisory practice roles spanning corporate strategy, operations, commercial finance, enterprise technology, and workforce planning.",
            "team.html",
            "team",
            team_body
        ))
    print("Page 21: team.html written.")

    # ====================================================
    # 22. insights.html
    # ====================================================
    articles_data = [
        ("How to Build a Business Growth Strategy", "strategy", "A structured guide to assessing market positioning, unit economics, and execution horizons before committing growth capital.", "7 min read", "article-art1.webp"),
        ("Why Business Process Assessment Matters", "operations", "How unmonitored operational handoffs accumulate cycle time variance and erode gross margins quietly.", "6 min read", "article-art2.webp"),
        ("Understanding Financial Planning for Businesses", "finance", "Moving beyond historical bookkeeping toward proactive rolling forecasts and working capital management.", "8 min read", "article-art3.webp"),
        ("How Digital Transformation Changes Operations", "technology", "Why successful digitization begins with workflow simplification rather than expensive enterprise software purchases.", "5 min read", "article-art4.webp"),
        ("Common Startup Planning Challenges", "startups", "Examining early-stage traps: premature scaling, unverified customer acquisition funnels, and poor cash runway visibility.", "6 min read", "article-art5.webp"),
        ("How to Improve Organizational Efficiency", "management", "Diagnosing management layers, spans of control, and decision rights to accelerate execution velocity.", "7 min read", "article-art6.webp"),
        ("Building a Practical Technology Roadmap", "technology", "A phased architecture approach to upgrading core enterprise systems without disrupting live operations.", "8 min read", "article-art7.webp"),
        ("Understanding Business Risk Management", "risk", "Why enterprise resilience requires cataloging single points of failure across supply chains and key personnel.", "6 min read", "article-art8.webp"),
    ]

    art_cards_html = []
    for title, cat, summary, time_read, img_file in articles_data:
        p_img = register_placeholder(
            "insights.html",
            f"Article Thumbnail - {title}",
            img_file,
            "aspect-16-9",
            "600x338",
            "Landscape",
            f"Corporate thought leadership editorial graphic representing {title}.",
            f"Corporate thought leadership business setting illustrating {title}. Professional corporate analytical environment, notebooks, strategic charts on modern displays, photorealistic commercial photography.",
            "Clean editorial medium shot with balanced subject placement.",
            "Soft ambient natural daylight.",
            "Contemporary corporate architectural workspace.",
            "Refined business editorial photography.",
            "Navy, charcoal grey, warm ochre, crisp white.",
            "Upper framing open."
        )

        art_cards_html.append(f'''
        <div class="card hover-lift filterable-item" data-category="{cat}">
          <div style="margin-bottom: 1.25rem;">{p_img}</div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.65rem;">
            <span class="demo-pill" style="font-size: 0.7rem; text-transform: uppercase;">{cat}</span>
            <span style="font-size: 0.78rem; color: var(--text-muted);">{time_read}</span>
          </div>
          <h3 class="card-title article-card-title">{title}</h3>
          <p class="card-desc article-card-desc">{summary}</p>
          <div class="card-footer">
            <a href="article-details.html" style="font-weight: 600;">Read Full Article &rarr;</a>
            <span class="demo-pill" style="font-size: 0.68rem; background: var(--warm-white);">Demo Content</span>
          </div>
        </div>
        ''')

    art_cards_joined = "\n".join(art_cards_html)

    ins_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Insights & Thought Leadership</li>
        </ul>
        <h1 class="page-hero-title">Business Insights & Advisory Perspectives</h1>
        <p class="page-hero-desc">Practical frameworks, diagnostic checklists, and strategic commentary addressing core enterprise challenges.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Live Search & Filter Bar -->
        <div style="max-width: 650px; margin: 0 auto 2.5rem; text-align: center;">
          <input type="text" id="insights-search" class="form-control" placeholder="Search insights by topic or keyword (e.g., strategy, process, risk)..." style="padding: 0.85rem 1.25rem; font-size: 1rem; border-radius: 99px; box-shadow: var(--shadow-sm);">
        </div>

        <div class="filter-bar">
          <button class="filter-btn active" data-filter="all">All Topics</button>
          <button class="filter-btn" data-filter="strategy">Strategy</button>
          <button class="filter-btn" data-filter="operations">Operations</button>
          <button class="filter-btn" data-filter="finance">Finance</button>
          <button class="filter-btn" data-filter="technology">Technology</button>
          <button class="filter-btn" data-filter="startups">Startups</button>
          <button class="filter-btn" data-filter="management">Management</button>
          <button class="filter-btn" data-filter="risk">Risk</button>
        </div>

        <div class="grid-3">
{art_cards_joined}
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "insights.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Insights & Articles | Business Strategy & Management Thought Leadership",
            "Editorial insights and business analysis on corporate strategy, process optimization, financial planning, digital transformation, and risk governance.",
            "insights.html",
            "insights",
            ins_body
        ))
    print("Page 22: insights.html written.")

    # ====================================================
    # 23. article-details.html
    # ====================================================
    img_artd = register_placeholder(
        "article-details.html",
        "Article Editorial Hero",
        "article-growth-strategy-hero.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Strategic planning charts and executive notes on a sleek boardroom conference table.",
        "Overhead editorial perspective of a clean corporate conference table with a bound business strategy report, fountain pen, and financial graphs on a tablet. Warm architectural morning sunlight, minimalist corporate aesthetic, photorealistic editorial photography.",
        "Flat-lay overhead angle with balanced composition of business documents.",
        "Warm natural morning daylight streaming across the surface.",
        "Rich dark walnut conference table surface.",
        "High-end corporate editorial photography.",
        "Deep walnut, crisp white paper, navy accents, brass pen.",
        "Generous negative space across the table surface."
    )

    artd_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="insights.html">Insights</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Article Details</li>
        </ul>
        <div style="display: flex; gap: 0.75rem; align-items: center; margin-bottom: 0.75rem;">
          <span class="demo-pill">Business Strategy</span>
          <span style="font-size: 0.8125rem; color: #C0CFE2;">7 Min Read &bull; Sample Editorial Content</span>
        </div>
        <h1 class="page-hero-title">How to Build a Business Growth Strategy</h1>
        <p class="page-hero-desc">A disciplined framework for evaluating addressable market dynamics, stress-testing unit economics, and aligning operational capacity before committing expansion capital.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="max-width: 860px; margin: 0 auto;">
          <div style="margin-bottom: 2.5rem;">{img_artd}</div>

          <div style="background: var(--blue-subtle); border-left: 4px solid var(--blue-accent); padding: 1.25rem; border-radius: var(--radius-sm); margin-bottom: 2.5rem;">
            <div style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--navy-primary); margin-bottom: 0.25rem;">Executive Summary</div>
            <p style="font-size: 0.95rem; line-height: 1.6; margin: 0; color: var(--text-main);">Growth initiatives fail more often from operational overextension than from lack of market demand. This article examines the three essential filters leadership teams must apply before executing a growth strategy: market validation, unit economics viability, and operational capacity calibration.</p>
          </div>

          <h2 style="font-size: 1.85rem; color: var(--navy-primary); margin-bottom: 1rem;">1. Differentiating Growth Ambition From Strategy</h2>
          <p>Too often, business growth plans resemble aspirational sales targets rather than coherent strategies. A target such as "achieve 30% top-line revenue expansion" is a metric, not a strategy. Strategy defines the precise mechanism: which customer segments will be acquired, why they will choose your offering over incumbents, and what trade-offs the enterprise will make to fulfill that demand profitably.</p>

          <h2 style="font-size: 1.85rem; color: var(--navy-primary); margin: 2rem 0 1rem;">2. Stress-Testing the Unit Economics</h2>
          <p>Accelerating sales volume through an unprofitable or fragile unit economics model only amplifies losses. Before launching aggressive expansion campaigns, leadership must examine:</p>
          <ul style="padding-left: 1.5rem; margin-bottom: 1.5rem;">
            <li><strong>Customer Acquisition Cost (CAC) by Channel:</strong> Are blended customer acquisition figures concealing underperforming marketing channels?</li>
            <li><strong>Gross Contribution Margin:</strong> Does each incremental transaction cover variable fulfillment costs and contribute realistically toward fixed overhead?</li>
            <li><strong>Payback Velocity:</strong> How many months of operating cash flow are required to recoup the capital expended to win each customer?</li>
          </ul>

          <h2 style="font-size: 1.85rem; color: var(--navy-primary); margin: 2rem 0 1rem;">3. Calibrating Operational Capacity</h2>
          <p>Sales success without delivery capability results in compromised service quality, customer churn, and employee burnout. An effective growth strategy establishes formal operational thresholds: sales velocity is paced to match the onboarding and fulfillment capacity of delivery teams.</p>

          <div style="background: var(--warm-white); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.5rem; margin: 2.5rem 0;">
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">The Strategic Growth Checklist</h4>
            <ul style="padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary); margin: 0;">
              <li>Validated addressable market size based on verified customer pain points</li>
              <li>Unit economics showing healthy contribution margin before fixed overhead</li>
              <li>Delivery capacity model preventing overextension of core staff</li>
              <li>Clear governance checkpoints to review growth metrics monthly</li>
            </ul>
          </div>

          <div style="border-top: 1px solid var(--border-color); padding-top: 2rem; margin-top: 3rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
              <span style="font-size: 0.85rem; color: var(--text-muted);">Topic: Enterprise Strategy &bull; Demonstration Editorial Article</span>
            </div>
            <a href="book-consultation.html" class="btn btn-primary">Discuss Your Growth Strategy &rarr;</a>
          </div>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "article-details.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "How to Build a Business Growth Strategy | Consulting Insights",
            "A structured guide to evaluating market positioning, unit economics, and operational capacity before committing growth capital.",
            "article-details.html",
            "insights",
            artd_body
        ))
    print("Page 23: article-details.html written.")

    # ====================================================
    # 24. resources.html
    # ====================================================
    resources_data = [
        ("Business Strategy Checklist", "Strategy", "A 10-point diagnostic checklist for leadership teams evaluating corporate growth roadmaps.", "PDF Preview Format"),
        ("Startup Planning Checklist", "Startups", "Essential operational, legal, and financial milestones for early-stage ventures.", "PDF Preview Format"),
        ("Business Process Assessment Template", "Operations", "A structured framework to map departmental handoffs and isolate bottleneck cycle times.", "Spreadsheet Preview"),
        ("Digital Transformation Roadmap", "Technology", "A phased four-quarter template for modernizing manual enterprise workflows.", "Presentation Preview"),
        ("Financial Planning Worksheet", "Finance", "A multi-scenario budget modeling and working capital cash flow diagnostic guide.", "Spreadsheet Preview"),
        ("Project Planning Checklist", "Project Management", "Scope baseline, RAID log, and milestone governance checklist for PMO teams.", "PDF Preview Format"),
        ("Enterprise Risk Assessment Template", "Risk Management", "A standard 5x5 likelihood-versus-impact risk matrix and mitigation register.", "PDF Preview Format"),
    ]

    res_cards_html = []
    for title, cat, desc, fmt in resources_data:
        res_cards_html.append(f'''
        <div class="card hover-lift">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <span class="demo-pill" style="font-size: 0.7rem;">{cat}</span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">{fmt}</span>
          </div>
          <h3 class="card-title" style="font-size: 1.25rem;">{title}</h3>
          <p class="card-desc" style="font-size: 0.9rem;">{desc}</p>
          <div class="card-footer">
            <button class="btn btn-secondary btn-sm" onclick="alert('Static Website Demonstration: This resource is a sample preview template. In an active deployment, client resources are dispatched via verified advisory channels.');">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 4px;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              View Preview
            </button>
            <span class="demo-pill" style="font-size: 0.68rem; background: var(--warm-white);">Static Preview</span>
          </div>
        </div>
        ''')

    res_cards_joined = "\n".join(res_cards_html)

    res_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Resources</li>
        </ul>
        <h1 class="page-hero-title">Business Resource Library & Checklists</h1>
        <p class="page-hero-desc">Practical diagnostic worksheets, strategy checklists, and governance templates designed to assist business leaders in structuring operations.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="notice-box notice-info" style="margin-bottom: 3rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Demonstration Notice:</strong> This static website does not connect to backend file servers or user tracking databases. Resource cards are provided as structured previews and educational examples of typical consulting artifacts.
          </div>
        </div>

        <div class="grid-3">
{res_cards_joined}
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "resources.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Resource Library | Business Strategy Checklists & Templates",
            "Downloadable business strategy checklists, process assessment templates, financial worksheets, and risk registers.",
            "resources.html",
            "resources",
            res_body
        ))
    print("Page 24: resources.html written.")

generate_corp_pages()
