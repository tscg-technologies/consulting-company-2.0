import os
from build_helpers import get_page_shell, make_placeholder
from generate_pages_part1 import register_placeholder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_final_pages():
    # ====================================================
    # 25. pricing.html
    # ====================================================
    pricing_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Pricing & Engagement</li>
        </ul>
        <h1 class="page-hero-title">Consulting Engagement Models</h1>
        <p class="page-hero-desc">We structure our advisory engagements around clear deliverables, defined scopes, and measurable milestones to ensure complete commercial transparency.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Mandatory Fee Disclaimer -->
        <div class="notice-box" style="margin-bottom: 3.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Engagement Pricing Notice:</strong> Final consulting fees depend on scope, complexity, duration, expertise required, and agreed deliverables. Because every enterprise operates under unique conditions, we do not apply rigid retail pricing. The structures below illustrate our standard advisory engagement tiers.
          </div>
        </div>

        <!-- Three Illustrative Engagement Tiers -->
        <div class="grid-3" style="margin-bottom: 4rem;">
          <div class="pricing-card">
            <h3 class="pricing-title">Initial Business Assessment</h3>
            <p class="pricing-scope">Targeted diagnostic for organizations seeking rapid clarity on an emerging challenge or strategic inflection point.</p>
            <div class="pricing-cta-price">Custom Proposal</div>
            <ul class="feature-list" style="margin-bottom: 2rem;">
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Comprehensive executive discovery interview</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Review of high-level operating & financial data</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Operational bottleneck & friction point inventory</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> High-level diagnostic summary & priority matrix</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Engagement duration: Typically 2 to 3 weeks</li>
            </ul>
            <div style="margin-top: auto;">
              <a href="book-consultation.html" class="btn btn-secondary btn-full">Request Assessment Scope</a>
            </div>
          </div>

          <div class="pricing-card featured">
            <div class="pricing-badge">Most Common Scope</div>
            <h3 class="pricing-title">Focused Consulting Engagement</h3>
            <p class="pricing-scope">In-depth practice advisory to solve a specific functional problem (operations, strategy, finance, or HR).</p>
            <div class="pricing-cta-price">Custom Proposal</div>
            <ul class="feature-list" style="margin-bottom: 2rem;">
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> End-to-end operational diagnostic & root cause analysis</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Stakeholder interviews across operational layers</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Target Operating Model (TOM) & process maps</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Phased 90-day implementation roadmap & RACI matrix</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Bi-weekly steering check-ins during delivery</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Engagement duration: Typically 6 to 12 weeks</li>
            </ul>
            <div style="margin-top: auto;">
              <a href="book-consultation.html" class="btn btn-primary btn-full">Request Focused Proposal</a>
            </div>
          </div>

          <div class="pricing-card">
            <h3 class="pricing-title">Custom Strategic Consulting</h3>
            <p class="pricing-scope">Comprehensive enterprise transformation spanning multiple functional practices and long-term advisory support.</p>
            <div class="pricing-cta-price">Custom Proposal</div>
            <ul class="feature-list" style="margin-bottom: 2rem;">
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Multi-disciplinary consulting team deployment</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Enterprise-wide diagnostic across strategy, ops, tech</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Board-level presentations and steering governance</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Multi-year strategic horizon planning & financial models</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Phased implementation governance & transition oversight</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Engagement duration: Tailored multi-month scope</li>
            </ul>
            <div style="margin-top: auto;">
              <a href="book-consultation.html" class="btn btn-secondary btn-full">Request Enterprise Proposal</a>
            </div>
          </div>
        </div>

        <!-- Scope Comparison Table -->
        <div class="section-header text-center">
          <span class="eyebrow">Scope Comparison</span>
          <h2 class="section-title">Engagement Deliverables Comparison</h2>
          <p class="section-subtitle">A side-by-side view of deliverables included across our advisory tiers.</p>
        </div>

        <div style="overflow-x: auto;">
          <table class="risk-matrix-table" style="text-align: left;">
            <thead>
              <tr>
                <th style="text-align: left; width: 40%;">Scope Deliverable</th>
                <th style="width: 20%;">Initial Assessment</th>
                <th style="width: 20%;">Focused Engagement</th>
                <th style="width: 20%;">Custom Strategic</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Executive Discovery & Objective Definition</td>
                <td style="text-align: center;">Included</td>
                <td style="text-align: center;">Included</td>
                <td style="text-align: center;">Included</td>
              </tr>
              <tr>
                <td>Current-State Diagnostic Report</td>
                <td style="text-align: center;">Executive Brief</td>
                <td style="text-align: center;">Comprehensive</td>
                <td style="text-align: center;">Enterprise-Wide</td>
              </tr>
              <tr>
                <td>Detailed Process Flow & Architecture Mapping</td>
                <td style="text-align: center;">High-Level</td>
                <td style="text-align: center;">Full Workstream</td>
                <td style="text-align: center;">Multi-Departmental</td>
              </tr>
              <tr>
                <td>RACI & Governance Framework</td>
                <td style="text-align: center;">&mdash;</td>
                <td style="text-align: center;">Included</td>
                <td style="text-align: center;">Included</td>
              </tr>
              <tr>
                <td>Target Operating Model (TOM)</td>
                <td style="text-align: center;">&mdash;</td>
                <td style="text-align: center;">Included</td>
                <td style="text-align: center;">Included</td>
              </tr>
              <tr>
                <td>Implementation Roadmap & Milestones</td>
                <td style="text-align: center;">Priority Matrix</td>
                <td style="text-align: center;">90-Day Plan</td>
                <td style="text-align: center;">Multi-Phase Schedule</td>
              </tr>
              <tr>
                <td>Post-Recommendation Steering Checkpoints</td>
                <td style="text-align: center;">&mdash;</td>
                <td style="text-align: center;">Bi-Weekly</td>
                <td style="text-align: center;">Steering Committee Cadence</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Request a Custom Proposal</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "pricing.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Engagement Framework & Pricing | Transparent Consulting Models",
            "Consulting engagement models and scope comparison. Initial business assessments, focused practice advisory, and custom strategic consulting.",
            "pricing.html",
            "pricing",
            pricing_body
        ))
    print("Page 25: pricing.html written.")

    # ====================================================
    # 26. careers.html
    # ====================================================
    careers_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Careers</li>
        </ul>
        <h1 class="page-hero-title">Consulting Practice Opportunities</h1>
        <p class="page-hero-desc">We welcome analytical thinkers, operational practitioners, and strategic problem solvers dedicated to delivering unvarnished business clarity.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Mandatory Careers Disclaimer -->
        <div class="notice-box" style="margin-bottom: 3.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Demonstration Recruitment Notice:</strong> The career opportunities and roles displayed below represent illustrative job profiles within a corporate management consulting firm. This website is a static demonstration and does not conduct live hiring campaigns, store resumes, or make contractual employment offers.
          </div>
        </div>

        <div class="section-header">
          <span class="eyebrow">Sample Practice Openings</span>
          <h2 class="section-title">Illustrative Consulting Roles</h2>
          <p class="section-subtitle">Typical positions across our advisory disciplines.</p>
        </div>

        <div class="grid-2" style="margin-bottom: 4rem;">
          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="demo-pill" style="font-size: 0.7rem;">Strategy Practice</span>
              <span class="demo-disclaimer-tag">Illustrative Role</span>
            </div>
            <h3 class="card-title">Senior Strategy Consultant</h3>
            <p class="card-desc">Leading corporate market research, unit economics stress testing, competitive positioning, and formulating multi-year strategic execution roadmaps.</p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="demo-pill" style="font-size: 0.7rem;">Operations Practice</span>
              <span class="demo-disclaimer-tag">Illustrative Role</span>
            </div>
            <h3 class="card-title">Operations Process Analyst</h3>
            <p class="card-desc">Conducting on-site workflow audits, mapping supply chain bottlenecks, and developing Lean standard operating procedures (SOPs).</p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="demo-pill" style="font-size: 0.7rem;">Financial Practice</span>
              <span class="demo-disclaimer-tag">Illustrative Role</span>
            </div>
            <h3 class="card-title">Commercial Financial Analyst</h3>
            <p class="card-desc">Building rolling financial forecast models, cost center diagnostics, and gross margin contribution analyses for enterprise clients.</p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span class="demo-pill" style="font-size: 0.7rem;">Early Career</span>
              <span class="demo-disclaimer-tag">Illustrative Role</span>
            </div>
            <h3 class="card-title">Consulting Associate / Intern</h3>
            <p class="card-desc">Supporting diagnostic research, synthesizing client workshop findings, and structuring analytical presentations under practice mentorship.</p>
          </div>
        </div>

        <!-- Frontend-Only Candidate Profile Form -->
        <div style="max-width: 760px; margin: 0 auto; background: var(--warm-white); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 2.5rem;">
          <div class="section-header text-center" style="margin-bottom: 2rem;">
            <span class="eyebrow">Candidate Submission Demo</span>
            <h3 style="font-size: 1.5rem; color: var(--navy-primary);">Submit an Illustrative Profile</h3>
            <p style="font-size: 0.9rem; color: var(--text-secondary);">Test our frontend form validation. No resume files or private records are uploaded.</p>
          </div>

          <form id="careers-form" novalidate>
            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Full Name <span class="required">*</span></label>
                <input type="text" class="form-control" required placeholder="Jane Doe">
              </div>
              <div class="form-group">
                <label class="form-label">Email Address <span class="required">*</span></label>
                <input type="email" class="form-control" required placeholder="candidate@example.com">
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Practice Area of Interest <span class="required">*</span></label>
                <select class="form-select" required>
                  <option value="">Select Practice...</option>
                  <option value="Strategy">Strategy Consulting</option>
                  <option value="Operations">Operations Consulting</option>
                  <option value="Finance">Financial Consulting</option>
                  <option value="Technology">Technology & Digital</option>
                  <option value="HR">HR & Workforce</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label">Years of Relevant Experience <span class="required">*</span></label>
                <select class="form-select" required>
                  <option value="">Select Range...</option>
                  <option value="0-2">0–2 Years (Associate)</option>
                  <option value="3-5">3–5 Years (Consultant)</option>
                  <option value="6-10">6–10 Years (Senior / Manager)</option>
                  <option value="10+">10+ Years (Practice Leader)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Professional Background Summary <span class="required">*</span></label>
              <textarea class="form-control" rows="4" required placeholder="Briefly describe your advisory background, key skills, and problem-solving focus..."></textarea>
            </div>

            <div class="notice-box notice-info" style="font-size: 0.8rem; margin-bottom: 1.5rem;">
              <strong>Static Demo Notice:</strong> Clicking submit triggers client-side validation only. No personal data will be recorded.
            </div>

            <button type="submit" class="btn btn-primary btn-full btn-lg">Submit Demonstration Profile</button>
          </form>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "careers.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Careers & Opportunities | Consulting Practice Openings",
            "Consulting practice career profiles: strategy consulting, operations analysis, financial modeling, technology advisory, and associate roles.",
            "careers.html",
            "careers",
            careers_body
        ))
    print("Page 26: careers.html written.")

    # ====================================================
    # 27. faq.html
    # ====================================================
    faq_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Frequently Asked Questions</li>
        </ul>
        <h1 class="page-hero-title">Frequently Asked Questions</h1>
        <p class="page-hero-desc">Clear answers regarding our consulting services, engagement scoping, methodology, and advisory collaboration models.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container container-narrow">
        <div class="accordion">
          <!-- Q1 -->
          <div class="accordion-item active">
            <button class="accordion-header" aria-expanded="true">
              <span>What does a consulting company do?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>A business consulting firm provides objective, external diagnostic analysis and strategic guidance. We partner with business leaders to identify operational bottlenecks, evaluate market opportunities, structure governance frameworks, and design realistic execution roadmaps to improve performance.</p>
            </div>
          </div>

          <!-- Q2 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>What types of consulting services are available?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>We offer 13 distinct practice areas: Business Consulting, Management Consulting, Strategy Consulting, Financial Consulting, HR Consulting, Marketing Consulting, IT Consulting, Digital Transformation, Operations Consulting, Startup Consulting, Risk Management, Project Management, and Organizational Development.</p>
            </div>
          </div>

          <!-- Q3 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>How does a consulting engagement begin?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Every engagement begins with an initial exploratory discussion where we examine your business context, core obstacles, and desired outcomes. Following this discussion, we prepare a formal engagement scope outlining the proposed diagnostic approach, required deliverables, timeline, and fee structure.</p>
            </div>
          </div>

          <!-- Q4 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>What information is required before an assessment?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Before launching a diagnostic review, we typically request high-level organizational charts, relevant operational process maps, recent management performance reports, and an overview of current business systems. All information is handled under strict confidentiality.</p>
            </div>
          </div>

          <!-- Q5 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>How long does a consulting engagement take?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Engagement duration depends on project complexity. An Initial Business Assessment typically takes 2 to 3 weeks; a Focused Consulting Engagement spans 6 to 12 weeks; while enterprise-wide strategic transformation roadmaps may extend over several months with structured quarterly review gates.</p>
            </div>
          </div>

          <!-- Q6 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>Can consulting services be customized?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Yes. Many enterprise challenges involve intersecting functional domains—for instance, combining operational workflow redesign with digital tool selection and workforce restructuring. We assemble bespoke, cross-functional advisory scopes aligned exactly with client needs.</p>
            </div>
          </div>

          <!-- Q7 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>Do you support implementation?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Yes. Where included in the agreed scope of work, our consultants provide steering committee governance, milestone reviews, transition oversight, and periodic recalibration sessions to ensure internal teams implement recommendations effectively.</p>
            </div>
          </div>

          <!-- Q8 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>How are consulting fees calculated?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Consulting fees are calculated based on engagement scope, required technical depth, duration, and agreed deliverables. We avoid hidden fees by establishing transparent, fixed-scope proposals before any billable work begins.</p>
            </div>
          </div>

          <!-- Q9 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>Can startups request consulting?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Yes. Our Startup Consulting practice is specifically designed for early-stage ventures and entrepreneurs looking to validate business models, design go-to-market funnels, pressure-test unit economics, and prepare structured pitch materials.</p>
            </div>
          </div>

          <!-- Q10 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>Do you provide remote consulting?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>Yes. We offer fully remote and hybrid advisory engagements. Using collaborative digital workshops, video steering reviews, and secure file exchanges, we deliver thorough consulting outcomes regardless of geographic location.</p>
            </div>
          </div>

          <!-- Q11 -->
          <div class="accordion-item">
            <button class="accordion-header" aria-expanded="false">
              <span>How can I schedule an initial consultation?</span>
              <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="accordion-body">
              <p>You can initiate an exploratory discussion by visiting our Book Consultation page or completing our Contact form. Our team will review your business challenge and connect to arrange a structured introductory call.</p>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <p style="color: var(--text-secondary); margin-bottom: 1rem;">Have a specific question not covered here?</p>
          <a href="contact.html" class="btn btn-secondary">Contact Our Advisory Desk &rarr;</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "faq.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Frequently Asked Questions (FAQ) | Consulting Inquiries",
            "Common questions regarding our consulting services, engagement processes, methodology, pricing calculations, startup advisory, and remote collaboration.",
            "faq.html",
            "faq",
            faq_body
        ))
    print("Page 27: faq.html written.")

    # ====================================================
    # 28. contact.html
    # ====================================================
    contact_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Contact</li>
        </ul>
        <h1 class="page-hero-title">Let's Discuss Your Business Challenges</h1>
        <p class="page-hero-desc">Reach out to our advisory desk to discuss your organization's strategic priorities, operational friction, or custom consulting requirements.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="gap: 3.5rem;">
          <!-- Contact Details Column -->
          <div>
            <span class="eyebrow">Advisory Desk</span>
            <h2 class="section-title">Get in Touch With Our Practice Leads</h2>
            <p class="lead">Every meaningful business partnership begins with an honest, structured conversation.</p>
            <p>Whether you require a focused diagnostic of current operations or a multi-year corporate strategy roadmap, we welcome your inquiry.</p>

            <div style="background: var(--blue-subtle); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.75rem; margin: 2rem 0;">
              <h4 style="color: var(--navy-primary); margin-bottom: 1.25rem;">Demonstration Contact Information</h4>
              
              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--navy-primary); flex-shrink: 0; margin-top: 2px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                <div>
                  <div style="font-weight: 600; color: var(--navy-primary);">Phone Numbers</div>
                  <div style="font-size: 0.9rem; color: var(--text-secondary);">Primary: 0000000000</div>
                  <div style="font-size: 0.9rem; color: var(--text-secondary);">Alternative: 0000000000</div>
                </div>
              </div>

              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--navy-primary); flex-shrink: 0; margin-top: 2px;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                <div>
                  <div style="font-weight: 600; color: var(--navy-primary);">Email Address</div>
                  <div style="font-size: 0.9rem; color: var(--text-secondary);"><a href="mailto:demo@example.com">demo@example.com</a></div>
                </div>
              </div>

              <div style="display: flex; gap: 0.75rem; margin-bottom: 1rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--navy-primary); flex-shrink: 0; margin-top: 2px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                <div>
                  <div style="font-weight: 600; color: var(--navy-primary);">Office Location</div>
                  <div style="font-size: 0.9rem; color: var(--text-secondary);">Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.</div>
                </div>
              </div>

              <div style="display: flex; gap: 0.75rem;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--navy-primary); flex-shrink: 0; margin-top: 2px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                <div>
                  <div style="font-weight: 600; color: var(--navy-primary);">Working Hours</div>
                  <div style="font-size: 0.9rem; color: var(--text-secondary);">Monday–Saturday: 9:00 AM–6:00 PM</div>
                </div>
              </div>
            </div>

            <div class="demo-disclaimer-tag">
              * Demonstration placeholders only &bull; Non-commercial website
            </div>
          </div>

          <!-- Contact Form Column -->
          <div style="background: var(--warm-white); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 2.25rem;">
            <h3 style="font-size: 1.4rem; color: var(--navy-primary); margin-bottom: 0.5rem;">Send an Advisory Inquiry</h3>
            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1.5rem;">Complete the form below. Client-side validation active; no external transmission.</p>

            <form id="contact-form" novalidate>
              <div class="form-group">
                <label class="form-label">Full Name <span class="required">*</span></label>
                <input type="text" class="form-control" required placeholder="Alexander Vance">
              </div>

              <div class="grid-2">
                <div class="form-group">
                  <label class="form-label">Email Address <span class="required">*</span></label>
                  <input type="email" class="form-control" required placeholder="alexander@organization.com">
                </div>
                <div class="form-group">
                  <label class="form-label">Phone Number <span class="required">*</span></label>
                  <input type="tel" class="form-control" required placeholder="0000000000">
                </div>
              </div>

              <div class="grid-2">
                <div class="form-group">
                  <label class="form-label">Organization Name <span class="required">*</span></label>
                  <input type="text" class="form-control" required placeholder="Acme Enterprises">
                </div>
                <div class="form-group">
                  <label class="form-label">Industry <span class="required">*</span></label>
                  <select class="form-select" required>
                    <option value="">Select Industry...</option>
                    <option value="Manufacturing">Manufacturing</option>
                    <option value="Healthcare">Healthcare</option>
                    <option value="Technology">Technology</option>
                    <option value="Retail">Retail & E-commerce</option>
                    <option value="Financial">Financial Services</option>
                    <option value="Logistics">Logistics & Supply Chain</option>
                    <option value="Other">Other Specialized Domain</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label">Consulting Service Required <span class="required">*</span></label>
                <select class="form-select" required>
                  <option value="">Select Practice Area...</option>
                  <option value="Business Consulting">Business Consulting</option>
                  <option value="Management Consulting">Management Consulting</option>
                  <option value="Strategy Consulting">Strategy Consulting</option>
                  <option value="Financial Consulting">Financial Consulting</option>
                  <option value="HR Consulting">HR Consulting</option>
                  <option value="Marketing Consulting">Marketing Consulting</option>
                  <option value="IT Consulting">IT Consulting</option>
                  <option value="Digital Transformation">Digital Transformation</option>
                  <option value="Operations Consulting">Operations Consulting</option>
                  <option value="Startup Consulting">Startup Consulting</option>
                  <option value="Risk Management">Risk Management</option>
                  <option value="Project Management">Project Management</option>
                  <option value="Organizational Development">Organizational Development</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label">Brief Description of the Challenge <span class="required">*</span></label>
                <textarea class="form-control" rows="4" required placeholder="Summarize your current operational friction, strategic question, or timeline expectations..."></textarea>
              </div>

              <div class="notice-box notice-info" style="font-size: 0.8rem; margin-bottom: 1.5rem;">
                <strong>Demonstration Form:</strong> Submissions in this demo are processed purely on the frontend. No personal data is saved.
              </div>

              <button type="submit" class="btn btn-primary btn-full btn-lg">Submit Demonstration Inquiry</button>
            </form>
          </div>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Contact Us | Let's Discuss Your Business Challenges",
            "Connect with our consulting advisory desk. Dummy demonstration office details, phone, email, and inquiry form.",
            "contact.html",
            "contact",
            contact_body
        ))
    print("Page 28: contact.html written.")

    # ====================================================
    # 29. book-consultation.html (6-Step Multi-Step Wizard)
    # ====================================================
    book_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Book Consultation</li>
        </ul>
        <h1 class="page-hero-title">Start With a Conversation. Move Forward With Clarity.</h1>
        <p class="page-hero-desc">Complete our structured 6-step consultation planner to help our practice leaders prepare for an exploratory discussion.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container container-narrow">
        <!-- Interactive Multi-Step Consultation Wizard -->
        <form id="consultation-wizard" novalidate>
          <!-- Progress Tracker Nodes -->
          <div class="wizard-progress">
            <div class="wizard-progress-bar" style="width: 0%;"></div>
            
            <div class="wizard-step-node active" data-step="1">
              <div class="wizard-node-circle">1</div>
              <span class="wizard-node-label">Contact</span>
            </div>
            <div class="wizard-step-node" data-step="2">
              <div class="wizard-node-circle">2</div>
              <span class="wizard-node-label">Business</span>
            </div>
            <div class="wizard-step-node" data-step="3">
              <div class="wizard-node-circle">3</div>
              <span class="wizard-node-label">Services</span>
            </div>
            <div class="wizard-step-node" data-step="4">
              <div class="wizard-node-circle">4</div>
              <span class="wizard-node-label">Challenge</span>
            </div>
            <div class="wizard-step-node" data-step="5">
              <div class="wizard-node-circle">5</div>
              <span class="wizard-node-label">Preferences</span>
            </div>
            <div class="wizard-step-node" data-step="6">
              <div class="wizard-node-circle">6</div>
              <span class="wizard-node-label">Review</span>
            </div>
          </div>

          <!-- STEP 1: Contact Details -->
          <div class="wizard-panel active" data-step="1">
            <h3 style="color: var(--navy-primary); font-size: 1.4rem; margin-bottom: 0.5rem;">Step 1: Your Contact Details</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 2rem;">Please provide your basic professional contact coordinates.</p>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Full Name <span class="required">*</span></label>
                <input type="text" id="wiz-name" class="form-control" required placeholder="e.g. Eleanor Rigby">
              </div>
              <div class="form-group">
                <label class="form-label">Email Address <span class="required">*</span></label>
                <input type="email" id="wiz-email" class="form-control" required placeholder="e.g. e.rigby@company.com">
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Phone Number <span class="required">*</span></label>
                <input type="tel" id="wiz-phone" class="form-control" required placeholder="0000000000">
              </div>
              <div class="form-group">
                <label class="form-label">Organization Name <span class="required">*</span></label>
                <input type="text" id="wiz-org" class="form-control" required placeholder="e.g. Apex Corporation">
              </div>
            </div>

            <div class="wizard-nav-buttons" style="justify-content: flex-end;">
              <button type="button" class="btn btn-primary wizard-next-btn">Next: Business Information &rarr;</button>
            </div>
          </div>

          <!-- STEP 2: Business Information -->
          <div class="wizard-panel" data-step="2">
            <h3 style="color: var(--navy-primary); font-size: 1.4rem; margin-bottom: 0.5rem;">Step 2: Business Profile</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 2rem;">Tell us about your organization's industry context and operating scale.</p>

            <div class="form-group">
              <label class="form-label">Primary Industry <span class="required">*</span></label>
              <select id="wiz-industry" class="form-select" required>
                <option value="">Select Industry...</option>
                <option value="Manufacturing">Manufacturing</option>
                <option value="Healthcare">Healthcare</option>
                <option value="Technology & SaaS">Technology & SaaS</option>
                <option value="Retail & E-commerce">Retail & E-commerce</option>
                <option value="Financial Services">Financial Services</option>
                <option value="Logistics & Supply Chain">Logistics & Supply Chain</option>
                <option value="Professional Services">Professional Services</option>
                <option value="Education">Education</option>
                <option value="Other Commercial Domain">Other Commercial Domain</option>
              </select>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Organization Size <span class="required">*</span></label>
                <select id="wiz-size" class="form-select" required>
                  <option value="">Select Size...</option>
                  <option value="1-10 Employees">1–10 Employees (Startup / Boutique)</option>
                  <option value="11-50 Employees">11–50 Employees (Small Business)</option>
                  <option value="51-250 Employees">51–250 Employees (Mid-Market)</option>
                  <option value="250+ Employees">250+ Employees (Enterprise)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label">Business Stage <span class="required">*</span></label>
                <select id="wiz-stage" class="form-select" required>
                  <option value="">Select Stage...</option>
                  <option value="Early Validation">Early Stage / Idea Validation</option>
                  <option value="Rapid Growth">Scaling / Rapid Growth</option>
                  <option value="Established Core">Established Core Operations</option>
                  <option value="Turnaround / Restructure">Turnaround / Restructuring</option>
                </select>
              </div>
            </div>

            <div class="wizard-nav-buttons">
              <button type="button" class="btn btn-secondary wizard-prev-btn">&larr; Back</button>
              <button type="button" class="btn btn-primary wizard-next-btn">Next: Consulting Requirements &rarr;</button>
            </div>
          </div>

          <!-- STEP 3: Consulting Requirements -->
          <div class="wizard-panel" data-step="3">
            <h3 style="color: var(--navy-primary); font-size: 1.4rem; margin-bottom: 0.5rem;">Step 3: Consulting Requirements</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 2rem;">Select the primary practice domain relevant to your inquiry.</p>

            <div class="form-group">
              <label class="form-label">Required Practice Discipline <span class="required">*</span></label>
              <select id="wiz-service" class="form-select" required>
                <option value="">Select Consulting Practice...</option>
                <option value="Business Strategy Consulting">Strategy & Corporate Growth</option>
                <option value="Operations Consulting">Operations & Process Optimization</option>
                <option value="Commercial Financial Planning">Commercial Financial Analysis</option>
                <option value="Management & Governance">Management & Leadership Alignment</option>
                <option value="Digital Transformation">Digital Transformation & Technology</option>
                <option value="HR & Workforce Planning">HR & Workforce Strategy</option>
                <option value="Startup Advisory">Startup Advisory & Go-To-Market</option>
                <option value="Enterprise Risk Management">Enterprise Risk Management</option>
                <option value="Project Governance (PMO)">Project Management & Delivery PMO</option>
                <option value="Organizational Development">Organizational Development & Culture</option>
                <option value="Multi-Disciplinary Scope">Cross-Functional / Multi-Disciplinary Scope</option>
              </select>
            </div>

            <div class="wizard-nav-buttons">
              <button type="button" class="btn btn-secondary wizard-prev-btn">&larr; Back</button>
              <button type="button" class="btn btn-primary wizard-next-btn">Next: Describe Challenge &rarr;</button>
            </div>
          </div>

          <!-- STEP 4: Business Challenge -->
          <div class="wizard-panel" data-step="4">
            <h3 style="color: var(--navy-primary); font-size: 1.4rem; margin-bottom: 0.5rem;">Step 4: Your Business Challenge</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 2rem;">Briefly outline what operational obstacle or strategic decision you are facing.</p>

            <div class="form-group">
              <label class="form-label">Primary Challenge Description <span class="required">*</span></label>
              <textarea id="wiz-challenge" class="form-control" rows="4" required placeholder="Describe what is causing friction (e.g. process handoff delays, stagnant growth, high staff turnover, legacy software debt)..."></textarea>
            </div>

            <div class="wizard-nav-buttons">
              <button type="button" class="btn btn-secondary wizard-prev-btn">&larr; Back</button>
              <button type="button" class="btn btn-primary wizard-next-btn">Next: Consultation Preferences &rarr;</button>
            </div>
          </div>

          <!-- STEP 5: Consultation Preferences -->
          <div class="wizard-panel" data-step="5">
            <h3 style="color: var(--navy-primary); font-size: 1.4rem; margin-bottom: 0.5rem;">Step 5: Consultation Preferences</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 2rem;">Indicate how and when you prefer to conduct the initial discovery call.</p>

            <div class="form-group">
              <label class="form-label">Preferred Format <span class="required">*</span></label>
              <select id="wiz-format" class="form-select" required>
                <option value="Virtual Video Conference">Virtual Video Conference (Secure Meeting Link)</option>
                <option value="Telephone Discussion">Direct Telephone Discussion</option>
                <option value="In-Person at Corporate Office">In-Person Meeting (Hyderabad Demo Suite)</option>
              </select>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Preferred Date <span class="required">*</span></label>
                <input type="date" id="wiz-date" class="form-control" required>
              </div>
              <div class="form-group">
                <label class="form-label">Preferred Time Window <span class="required">*</span></label>
                <select id="wiz-time" class="form-select" required>
                  <option value="Morning (9:00 AM – 12:00 PM)">Morning (9:00 AM – 12:00 PM)</option>
                  <option value="Afternoon (1:00 PM – 4:00 PM)">Afternoon (1:00 PM – 4:00 PM)</option>
                  <option value="Late Afternoon (4:00 PM – 6:00 PM)">Late Afternoon (4:00 PM – 6:00 PM)</option>
                </select>
              </div>
            </div>

            <div class="wizard-nav-buttons">
              <button type="button" class="btn btn-secondary wizard-prev-btn">&larr; Back</button>
              <button type="button" class="btn btn-primary wizard-next-btn">Next: Review Brief &rarr;</button>
            </div>
          </div>

          <!-- STEP 6: Review & Submit -->
          <div class="wizard-panel" data-step="6">
            <h3 style="color: var(--navy-primary); font-size: 1.4rem; margin-bottom: 0.5rem;">Step 6: Review Your Consultation Brief</h3>
            <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 2rem;">Please verify your details prior to submitting this demonstration request.</p>

            <ul class="review-summary-list" style="margin-bottom: 2rem;">
              <li class="review-item">
                <div class="review-item-label">Full Name</div>
                <div class="review-item-value" id="rev-name">--</div>
              </li>
              <li class="review-item">
                <div class="review-item-label">Email Address</div>
                <div class="review-item-value" id="rev-email">--</div>
              </li>
              <li class="review-item">
                <div class="review-item-label">Phone & Organization</div>
                <div class="review-item-value"><span id="rev-phone">--</span> &bull; <span id="rev-org">--</span></div>
              </li>
              <li class="review-item">
                <div class="review-item-label">Industry & Stage</div>
                <div class="review-item-value"><span id="rev-industry">--</span> (<span id="rev-stage">--</span>)</div>
              </li>
              <li class="review-item">
                <div class="review-item-label">Consulting Practice</div>
                <div class="review-item-value" id="rev-service">--</div>
              </li>
              <li class="review-item">
                <div class="review-item-label">Preferred Session</div>
                <div class="review-item-value" id="rev-datetime">--</div>
              </li>
            </ul>

            <div class="review-item" style="margin-bottom: 2rem;">
              <div class="review-item-label">Summary of Challenge</div>
              <div class="review-item-value" id="rev-challenge" style="font-weight: 400; font-size: 0.9rem; line-height: 1.6;">--</div>
            </div>

            <div class="notice-box notice-info" style="font-size: 0.8rem; margin-bottom: 1.5rem;">
              <strong>Static Demo Environment:</strong> Clicking "Submit Consultation Request" executes client-side demo verification. No live emails or database records are generated.
            </div>

            <div class="wizard-nav-buttons">
              <button type="button" class="btn btn-secondary wizard-prev-btn">&larr; Back to Edit</button>
              <button type="button" class="btn btn-primary wizard-submit-btn btn-lg">Submit Consultation Request</button>
            </div>
          </div>
        </form>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "book-consultation.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Book a Consultation | Structured 6-Step Advisory Planner",
            "Schedule an exploratory business consultation. 6-step interactive consultation planner covering contact details, business profile, service requirements, and preferences.",
            "book-consultation.html",
            "book-consultation",
            book_body
        ))
    print("Page 29: book-consultation.html written.")

    # ====================================================
    # 30. privacy-policy.html
    # ====================================================
    privacy_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Privacy Policy</li>
        </ul>
        <h1 class="page-hero-title">Privacy Policy</h1>
        <p class="page-hero-desc">Information regarding data protection, cookies, demonstration forms, and confidentiality standards.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container container-narrow">
        <div class="notice-box" style="margin-bottom: 2.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          <div class="notice-content">
            <strong>Demonstration Legal Notice:</strong> This privacy policy document represents sample educational text tailored for a generic corporate consulting demonstration. It requires formal review and customization by qualified legal counsel prior to commercial deployment.
          </div>
        </div>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin-bottom: 0.75rem;">1. Demonstration Environment & Data Transmission</h2>
        <p>This website operates as a static frontend demonstration hosted on standard web infrastructure. Any information entered into our consultation wizards, contact forms, or careers submission fields is processed locally via client-side JavaScript. This website does not transmit, store, or serialize personal data across external databases, third-party marketing servers, or persistent tracking platforms.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">2. Cookies & Analytics</h2>
        <p>This static website does not set persistent tracking cookies, third-party behavioral profiling scripts, or retargeting pixels. Standard web server access logs maintained by hosting providers (such as Hostinger) may record generic network metadata (e.g. IP address, browser user-agent, and HTTP request headers) solely for infrastructure security and server diagnostic purposes.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">3. Client Confidentiality in Commercial Engagements</h2>
        <p>In a production consulting engagement, all client information, proprietary financial records, operational diagrams, and strategic discussions are governed by dedicated Non-Disclosure Agreements (NDAs) and professional confidentiality covenants executed prior to project discovery.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">4. Demonstration Contact Information</h2>
        <p>If you have questions regarding this demonstration website or its policies, please contact the demonstration coordinator at <a href="mailto:demo@example.com">demo@example.com</a>.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">5. Policy Updates</h2>
        <p>This sample policy was last updated in November 2026. Any future revisions will be posted directly to this page.</p>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "privacy-policy.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Privacy Policy | Demonstration Terms & Data Protection",
            "Demonstration privacy policy covering form data handling, cookies, server logs, client confidentiality standards, and legal disclaimers.",
            "privacy-policy.html",
            "privacy",
            privacy_body
        ))
    print("Page 30: privacy-policy.html written.")

    # ====================================================
    # 31. terms-and-conditions.html
    # ====================================================
    terms_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Terms & Conditions</li>
        </ul>
        <h1 class="page-hero-title">Terms & Conditions</h1>
        <p class="page-hero-desc">Standard terms governing the use of this demonstration consulting website and service descriptions.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container container-narrow">
        <div class="notice-box" style="margin-bottom: 2.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          <div class="notice-content">
            <strong>Demonstration Legal Notice:</strong> The terms and conditions set forth on this page constitute sample contractual material designed for demonstration purposes only. They do not constitute formal legal advice and require professional review by a licensed attorney prior to actual commercial utilization.
          </div>
        </div>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin-bottom: 0.75rem;">1. Acceptance of Terms</h2>
        <p>By accessing or browsing this website (the "Site"), you agree to be bound by these demonstration Terms & Conditions. If you do not agree with any portion of these terms, please discontinue use of this Site.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">2. Nature of Service Descriptions</h2>
        <p>The service descriptions, case studies, diagnostic diagrams, and engagement frameworks displayed on this Site are presented solely for illustrative and informational purposes. They do not constitute binding commercial offers, guaranteed operational outcomes, or statutory warranties of any kind.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">3. Absence of Regulated Advice</h2>
        <p>The materials published on this Site do not constitute certified public accounting, statutory audit, legal counsel, actuarial certification, or regulated investment advice. Users must seek independent licensed counsel for statutory compliance questions.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">4. Engagement Proposals & Scope of Work</h2>
        <p>Actual consulting engagements require the execution of a bespoke written Scope of Work (SOW) or Master Services Agreement (MSA) signed by authorized corporate representatives. No consulting relationship is created merely by submitting an inquiry via this Site.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">5. Intellectual Property</h2>
        <p>All page layouts, CSS designs, and structural source code are generic demonstration assets created for pair programming demonstration purposes.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">6. Limitation of Liability</h2>
        <p>To the fullest extent permitted by applicable law, CONSULTING COMPANY and its contributors disclaim all liability for any direct, indirect, incidental, or consequential damages resulting from the use of, or inability to use, the information published on this demonstration Site.</p>

        <h2 style="font-size: 1.5rem; color: var(--navy-primary); margin: 2rem 0 0.75rem;">7. Contact & Inquiries</h2>
        <p>For inquiries regarding these terms, contact <a href="mailto:demo@example.com">demo@example.com</a>.</p>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "terms-and-conditions.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Terms & Conditions | Demonstration Legal Guidelines",
            "Demonstration terms and conditions covering website usage, consulting service descriptions, proposals, confidentiality, and liability limitations.",
            "terms-and-conditions.html",
            "terms",
            terms_body
        ))
    print("Page 31: terms-and-conditions.html written.")

generate_final_pages()
