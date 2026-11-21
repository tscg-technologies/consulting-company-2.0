import os
from build_helpers import get_page_shell, make_placeholder
from generate_pages_part1 import register_placeholder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def generate_individual_services():
    # ----------------------------------------------------
    # 4. business-consulting.html
    # ----------------------------------------------------
    img_bc = register_placeholder(
        "business-consulting.html",
        "Practice Hero",
        "business-consulting-lead.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Senior business consultants reviewing comprehensive enterprise growth projections with business owners in an executive office.",
        "Two senior corporate consultants presenting an operational growth diagnostic on a high-resolution display to executive leadership. Well-appointed contemporary boardroom, warm architectural daylight, professional business attire, sharp focus, understated corporate luxury.",
        "Medium shot capturing the collaborative review and screen presentation.",
        "Bright natural daylight with gentle warm interior accents.",
        "Executive corner office with clean architectural wood paneling.",
        "High-end corporate documentary photography.",
        "Deep navy, slate grey, warm honey oak, crisp white.",
        "Clear upper framing for header balance."
    )

    bc_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Business Consulting</li>
        </ul>
        <h1 class="page-hero-title">Practical Business Advice for Your Next Stage of Growth</h1>
        <p class="page-hero-desc">We work with leadership teams to evaluate business models, identify operational bottlenecks, and formulate grounded business plans for sustainable commercial performance.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Practice Overview</span>
            <h2 class="section-title">Objective Diagnostics to Navigate Critical Business Inflections</h2>
            <p class="lead">Whether you are expanding into adjacent markets, restructuring legacy operations, or addressing revenue plateauing, our business consulting practice delivers rigorous commercial clarity.</p>
            <p>We analyze current business performance, conduct structured process reviews, and assess realistic market opportunities to construct actionable recommendations with measurable milestones.</p>
          </div>
          <div>{img_bc}</div>
        </div>

        <div class="section-header">
          <span class="eyebrow">Scope of Advisory</span>
          <h2 class="section-title">Core Advisory Capabilities</h2>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Business Model Evaluation</h3>
            <p class="card-desc">Reviewing customer segments, value propositions, cost dynamics, and revenue streams to validate long-term economic viability.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Market Opportunity Assessment</h3>
            <p class="card-desc">Evaluating competitive positioning, customer demand signals, and market entry barriers to target realistic growth avenues.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Business Process Review</h3>
            <p class="card-desc">Mapping operational handoffs, departmental dependencies, and resource allocations to eliminate systemic friction.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Performance Analysis</h3>
            <p class="card-desc">Establishing key operational performance indicators (KPIs) to track profitability, cycle times, and resource efficiency.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Strategic Recommendations</h3>
            <p class="card-desc">Delivering prioritized action plans with explicit trade-off analyses, resource requirements, and risk factors.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Implementation Planning</h3>
            <p class="card-desc">Translating high-level strategy into 90-day operational sprints, accountability matrices, and governance checkpoints.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-light-blue">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Engagement Lifecycle</span>
          <h2 class="section-title">Typical Consulting Deliverables</h2>
          <p class="section-subtitle">Every business consulting engagement concludes with tangible operational artifacts.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Comprehensive Diagnostic Report</h4>
            <p style="font-size: 0.88rem;">An unvarnished assessment of operating challenges, structural cost drivers, and organizational constraints.</p>
          </div>
          <div class="card">
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Target Operating Model (TOM)</h4>
            <p style="font-size: 0.88rem;">A structured blueprint detailing process handoffs, organizational responsibilities, and governance cadences.</p>
          </div>
          <div class="card">
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Strategic Execution Roadmap</h4>
            <p style="font-size: 0.88rem;">A prioritized implementation schedule with explicit workstreams, resource commitments, and quarterly review gates.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Schedule a Business Consultation</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "business-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Business Consulting Practice | Practical Growth Advice",
            "Practical business planning, business model evaluation, process reviews, and implementation roadmaps to structure organizations for sustainable commercial growth.",
            "business-consulting.html",
            "services",
            bc_body
        ))
    print("Page 4: business-consulting.html written.")

    # ----------------------------------------------------
    # 5. management-consulting.html
    # ----------------------------------------------------
    img_mc = register_placeholder(
        "management-consulting.html",
        "Practice Hero",
        "corporate-management-consulting.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Executive management advisory discussion focused on leadership structure and governance frameworks.",
        "Corporate management consulting team and executive directors seated at a minimalist conference table reviewing organizational governance charts. Professional atmosphere, dignified demeanor, balanced composition, soft corporate lighting.",
        "Medium-wide shot with clear depth of field.",
        "Diffused overhead LED architectural lighting with daylight accents.",
        "Refined corporate office with glass walls and minimalist architectural elements.",
        "Editorial corporate photography.",
        "Charcoal grey, navy, warm beige, crisp white.",
        "Top portion open for visual clarity."
    )

    mc_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Management Consulting</li>
        </ul>
        <h1 class="page-hero-title">Enhance Organizational Structure and Management Effectiveness</h1>
        <p class="page-hero-desc">We assist executive leadership in aligning organizational structures, streamlining decision-making frameworks, and strengthening management governance.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Governance & Performance</span>
            <h2 class="section-title">Aligning Leadership Strategy With Execution Architecture</h2>
            <p class="lead">As organizations scale, operational friction often stems not from market conditions, but from ambiguous accountability, fragmented reporting lines, and slow management processes.</p>
            <p>Our management consulting practice evaluates leadership alignment, optimizes organizational structures, and embeds structured decision-making mechanisms that empower managers to execute decisively.</p>
          </div>
          <div>{img_mc}</div>
        </div>

        <!-- Visual Management Framework Diagram -->
        <div class="section-header text-center">
          <span class="eyebrow">Operational Framework</span>
          <h2 class="section-title">The Four Pillars of Management Effectiveness</h2>
          <p class="section-subtitle">A balanced management model designed to sustain operational performance.</p>
        </div>

        <div class="grid-4" style="margin-bottom: 3.5rem;">
          <div class="card" style="border-top: 3px solid var(--navy-primary);">
            <div class="card-icon" style="background: var(--blue-subtle);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">1. Structure & RACI</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Clear delineation of roles: Responsible, Accountable, Consulted, and Informed across core processes.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--blue-secondary);">
            <div class="card-icon" style="background: var(--blue-subtle); color: var(--blue-secondary);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">2. Decision Frameworks</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Standardized escalation thresholds and delegated authorities to eliminate bureaucratic delays.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--blue-accent);">
            <div class="card-icon" style="background: var(--blue-light); color: var(--blue-accent);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">3. Performance Cadence</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Structured monthly operating reviews (MORs) and operational KPI scorecards for executive oversight.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--gold-accent);">
            <div class="card-icon" style="background: var(--gold-light); color: var(--gold-accent);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">4. Change Enablement</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Structured communication and stakeholder transition roadmaps to safeguard operational continuity.</p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <h3 class="card-title">Leadership Alignment Sessions</h3>
            <p class="card-desc">Facilitated executive workshops designed to resolve conflicting priorities, align departmental KPIs, and establish cohesive operational mandates across management tiers.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Organizational Efficiency Reviews</h3>
            <p class="card-desc">Analysis of spans of control, managerial layers, and functional overlaps to streamline administrative costs and improve information flow across the enterprise.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Consult on Management Governance</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "management-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Management Consulting Practice | Governance & Efficiency",
            "Management consulting services to optimize organizational structures, decision-making frameworks, leadership alignment, and enterprise management efficiency.",
            "management-consulting.html",
            "services",
            mc_body
        ))
    print("Page 5: management-consulting.html written.")

    # ----------------------------------------------------
    # 6. strategy-consulting.html
    # ----------------------------------------------------
    img_sc = register_placeholder(
        "strategy-consulting.html",
        "Practice Hero",
        "strategy-consulting-lead.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Strategy consultants mapping market expansion horizons and competitive matrices on a modern glass wall.",
        "Senior corporate strategy advisor drawing an illustrative strategic horizon framework on a floor-to-ceiling glass partition in a sunlit executive meeting room. Executive team observing attentively. Modern minimalist interior, ultra-high detail, professional corporate photography.",
        "Medium shot with strong diagonal leading lines from the glass chart to the consultants.",
        "Natural directional morning light with gentle fill.",
        "Contemporary corporate glass suite with panoramic city skyline.",
        "Clean editorial business photography.",
        "Navy primary, deep indigo, warm white, subtle gold accents.",
        "Generous negative space on the right side."
    )

    sc_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Strategy Consulting</li>
        </ul>
        <h1 class="page-hero-title">Turn Business Ambition Into a Clear Strategic Direction</h1>
        <p class="page-hero-desc">We help organizations assess market dynamics, define competitive advantages, and build realistic strategic execution roadmaps.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Strategic Direction</span>
            <h2 class="section-title">Rigorous Corporate Strategy Grounded in Market Realities</h2>
            <p class="lead">Strategy is not an aspirational statement—it is a coherent set of choices regarding where to compete, how to win, and what initiatives to deliberately decline.</p>
            <p>Our strategy consulting practice conducts market research, evaluates competitive positioning, assesses revenue models, and produces strategic execution roadmaps that translate ambitious goals into practical reality.</p>
          </div>
          <div>{img_sc}</div>
        </div>

        <!-- Strategic Planning Framework -->
        <div class="section-header text-center">
          <span class="eyebrow">Strategic Horizon Framework</span>
          <h2 class="section-title">Three Horizons of Strategic Growth</h2>
          <p class="section-subtitle">Balancing current operational core performance with future business expansion.</p>
        </div>

        <div class="grid-3" style="margin-bottom: 3rem;">
          <div class="card" style="border-top: 3px solid var(--navy-primary);">
            <span class="eyebrow" style="margin-bottom: 0.35rem;">Horizon 1</span>
            <h3 class="card-title">Defend & Optimize the Core</h3>
            <p class="card-desc">Strengthening existing revenue engines, refining pricing models, protecting market share against competitive encroachment, and improving operating margins.</p>
          </div>
          <div class="card" style="border-top: 3px solid var(--blue-accent);">
            <span class="eyebrow" style="margin-bottom: 0.35rem;">Horizon 2</span>
            <h3 class="card-title">Scale Emerging Opportunities</h3>
            <p class="card-desc">Entering adjacent customer segments, expanding geographic distribution channels, and launching validated extensions of existing service lines.</p>
          </div>
          <div class="card" style="border-top: 3px solid var(--gold-accent);">
            <span class="eyebrow" style="margin-bottom: 0.35rem;">Horizon 3</span>
            <h3 class="card-title">Build Future Capabilities</h3>
            <p class="card-desc">Evaluating disruptive business models, new technological capabilities, and strategic partnership options for multi-year enterprise longevity.</p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <h3 class="card-title">Competitive & Market Positioning</h3>
            <p class="card-desc">In-depth benchmarking of competitor pricing structures, value propositions, and customer churn triggers to formulate unique, defensible market positioning.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Strategic Execution Roadmaps</h3>
            <p class="card-desc">A structured operational playbook translating strategic priorities into 12-to-36-month roadmaps with explicit capital allocation requirements and operational milestones.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Explore Strategic Formulation</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "strategy-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Strategy Consulting Practice | Turn Ambition Into Direction",
            "Strategy consulting services for corporate growth, market research, competitive analysis, business expansion, and strategic execution roadmaps.",
            "strategy-consulting.html",
            "services",
            sc_body
        ))
    print("Page 6: strategy-consulting.html written.")

    # ----------------------------------------------------
    # 7. financial-consulting.html
    # ----------------------------------------------------
    img_fc = register_placeholder(
        "financial-consulting.html",
        "Practice Hero",
        "financial-consulting-dashboard.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Corporate financial consultant examining cash flow projections and budget modeling dashboards on dual monitors.",
        "Professional commercial financial advisor sitting in an executive office reviewing analytical financial modeling dashboards on dual high-resolution displays. Corporate financial worksheets, clean corporate desk, tasteful brass lighting, professional tone.",
        "Over-the-shoulder angle focusing on screen data models and consultant's analytical review.",
        "Balanced ambient interior light with crisp screen glow.",
        "Refined corporate office with bookmatched walnut timber details.",
        "High-end corporate commercial photography.",
        "Navy, warm gold, graphite, soft ivory.",
        "Balanced side negative space."
    )

    fc_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Financial Consulting</li>
        </ul>
        <h1 class="page-hero-title">Financial Performance Analysis and Commercial Planning</h1>
        <p class="page-hero-desc">We assist business owners and executives with commercial financial assessments, budget modeling, cash flow diagnostics, and cost rationalization frameworks.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Mandatory Regulatory Disclaimer -->
        <div class="notice-box">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          <div class="notice-content">
            <strong>Important Regulatory Notice:</strong> The services described herein represent general management consulting and operational commercial analysis. This firm does not provide regulated investment advice, statutory audit, legal, certified tax advisory, or public accounting services requiring specific statutory licenses. All figures, metrics, and models displayed on this website are illustrative demo mockups and do not constitute actual performance guarantees.
          </div>
        </div>

        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Commercial Diagnostics</span>
            <h2 class="section-title">Bringing Discipline and Transparency to Financial Decisions</h2>
            <p class="lead">Effective management requires unvarnished visibility into unit economics, contribution margins, and working capital cycles.</p>
            <p>Our financial consulting practice focuses on management accounting diagnostics, budgeting frameworks, cost driver reviews, and scenario planning so leadership can allocate capital with confidence.</p>
          </div>
          <div>{img_fc}</div>
        </div>

        <!-- Illustrative Financial Dashboard Mockup -->
        <div class="dashboard-preview" style="margin-bottom: 3.5rem;">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Illustrative Commercial Performance Dashboard</h4>
              <span>Cash Flow & Cost Variance Simulation &bull; Demo Modeling Representation</span>
            </div>
            <span class="demo-pill">Illustrative Demo Data</span>
          </div>

          <div class="dashboard-metrics-grid">
            <div class="metric-box">
              <div class="metric-label">Operating Cash Runway</div>
              <div class="metric-value">18.4 Months</div>
              <div class="metric-trend">&uarr; Target Liquidity Buffer</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Gross Margin Contribution</div>
              <div class="metric-value">46.2%</div>
              <div class="metric-trend">&bull; Peer Benchmark Median</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Fixed Overhead Ratio</div>
              <div class="metric-value">22.1%</div>
              <div class="metric-trend">&darr; Rationalized Baseline</div>
            </div>
          </div>

          <div class="grid-2">
            <div class="chart-container">
              <div class="chart-title">
                <span>Working Capital Projection by Quarter</span>
                <span style="font-size: 0.72rem; color: #8E9BAE;">Normalized Scale</span>
              </div>
              <div class="bar-chart-mock">
                <div class="bar-col"><div class="bar-fill" style="height: 50%;"></div><span class="bar-label">Q1 Base</span></div>
                <div class="bar-col"><div class="bar-fill" style="height: 65%;"></div><span class="bar-label">Q2 Est</span></div>
                <div class="bar-col"><div class="bar-fill gold" style="height: 78%;"></div><span class="bar-label">Q3 Proj</span></div>
                <div class="bar-col"><div class="bar-fill gold" style="height: 88%;"></div><span class="bar-label">Q4 Target</span></div>
              </div>
            </div>

            <div class="chart-container">
              <div class="chart-title">
                <span>Cost Center Allocation Review</span>
                <span style="font-size: 0.72rem; color: #8E9BAE;">Functional Share</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 0.65rem; padding-top: 0.5rem;">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>Direct Service Delivery & COGS</span><span>54%</span>
                  </div>
                  <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: var(--blue-accent); width: 54%; height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>Sales, Marketing & Acquisition</span><span>26%</span>
                  </div>
                  <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: var(--gold-accent); width: 26%; height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>General & Administrative</span><span>20%</span>
                  </div>
                  <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: #38C172; width: 20%; height: 100%;"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Budget Planning & Modeling</h3>
            <p class="card-desc">Establishing multi-scenario operating budgets, variance analysis mechanisms, and department spending limits to prevent cash shortfalls.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Cash Flow & Working Capital</h3>
            <p class="card-desc">Optimizing billing cycles, accounts receivable management, and supplier payment terms to protect operating liquidity.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Cost & Margin Diagnostics</h3>
            <p class="card-desc">Granular examination of direct and indirect overhead costs to identify margin leakage and support sustainable pricing adjustments.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Request Commercial Financial Assessment</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "financial-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Financial Consulting Practice | Performance & Commercial Planning",
            "Financial performance analysis, budgeting frameworks, cash flow planning, cost analysis, and management reporting for commercial decision-makers.",
            "financial-consulting.html",
            "services",
            fc_body
        ))
    print("Page 7: financial-consulting.html written.")

    # ----------------------------------------------------
    # 8. hr-consulting.html
    # ----------------------------------------------------
    img_hr = register_placeholder(
        "hr-consulting.html",
        "Practice Hero",
        "hr-consulting-team-meeting.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "HR consulting advisors discussing workforce capability matrices and talent management frameworks in a modern corporate setting.",
        "Human resources strategic consulting team analyzing workforce planning charts and talent retention models on an interactive whiteboard. Professional corporate office with glass walls, natural lighting, focused business attire, crisp photographic detail.",
        "Medium shot capturing the collaborative discussion around the talent framework.",
        "Bright natural daylight from wide windows.",
        "Corporate glass conference room with ergonomic furniture.",
        "Professional corporate commercial style.",
        "Navy, slate blue, warm light wood, white.",
        "Open space in the upper portion."
    )

    hr_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>HR Consulting</li>
        </ul>
        <h1 class="page-hero-title">Workforce Planning, Talent Strategy, and Performance Frameworks</h1>
        <p class="page-hero-desc">We help organizations design structured HR frameworks, workforce capacity models, and talent management processes that support strategic business objectives.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">People & Performance</span>
            <h2 class="section-title">Structuring Organizations for Talent Retention and Productivity</h2>
            <p class="lead">A company's operational execution is fundamentally bounded by the capability, alignment, and retention of its workforce.</p>
            <p>Our HR consulting practice delivers structured workforce planning, objective performance appraisal architectures, recruitment process reviews, and talent management frameworks that align individual output with corporate strategy.</p>
          </div>
          <div>{img_hr}</div>
        </div>

        <!-- Illustrative HR Dashboard & Workforce Planning Mockup -->
        <div class="dashboard-preview" style="margin-bottom: 3.5rem;">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Workforce Capability & Recruitment Pipeline Mockup</h4>
              <span>Illustrative Human Capital Framework &bull; Demo Analytics Representation</span>
            </div>
            <span class="demo-pill">Illustrative Demo Data</span>
          </div>

          <div class="dashboard-metrics-grid">
            <div class="metric-box">
              <div class="metric-label">Key Role Retention Index</div>
              <div class="metric-value">91.4%</div>
              <div class="metric-trend">&uarr; Target Stability Benchmark</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Recruitment Cycle Time</div>
              <div class="metric-value">28 Days</div>
              <div class="metric-trend">&darr; Optimized Hiring Velocity</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Performance Calibration Ratio</div>
              <div class="metric-value">84.2%</div>
              <div class="metric-trend">&bull; Balanced Evaluation Bell</div>
            </div>
          </div>

          <div class="chart-container">
            <div class="chart-title">
              <span>Departmental Headcount & Capacity Distribution</span>
              <span style="font-size: 0.72rem; color: #8E9BAE;">Functional Teams</span>
            </div>
            <div class="bar-chart-mock">
              <div class="bar-col"><div class="bar-fill" style="height: 75%;"></div><span class="bar-label">Engineering</span></div>
              <div class="bar-col"><div class="bar-fill" style="height: 55%;"></div><span class="bar-label">Operations</span></div>
              <div class="bar-col"><div class="bar-fill gold" style="height: 40%;"></div><span class="bar-label">Commercial</span></div>
              <div class="bar-col"><div class="bar-fill gold" style="height: 30%;"></div><span class="bar-label">Corporate G&A</span></div>
            </div>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Workforce Planning & Sizing</h3>
            <p class="card-desc">Analyzing workload distribution, skill gaps, and projected hiring requirements across operational departments.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Performance Management</h3>
            <p class="card-desc">Designing objective KPI scorecards, appraisal rubrics, and regular feedback mechanisms to foster high performance.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Recruitment Process Optimization</h3>
            <p class="card-desc">Evaluating candidate assessment protocols, interview scorecards, and hiring cycle bottlenecks to improve talent quality.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Compensation & Job Grading</h3>
            <p class="card-desc">Structuring internal job levels, title taxonomies, and transparent compensation bands aligned with industry benchmarks.</p>
          </div>
          <div class="card">
            <h3 class="card-title">HR Policy & Governance</h3>
            <p class="card-desc">Reviewing employee handbooks, onboarding protocols, and internal operational policies for clarity and compliance.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Learning & Succession Planning</h3>
            <p class="card-desc">Building competency matrices and succession roadmaps for mission-critical managerial and technical roles.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Schedule an HR Practice Consultation</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "hr-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "HR Consulting Practice | Workforce & Performance Strategy",
            "HR consulting services for workforce planning, recruitment process optimization, talent retention, performance management, and organizational structure.",
            "hr-consulting.html",
            "services",
            hr_body
        ))
    print("Page 8: hr-consulting.html written.")

    # ----------------------------------------------------
    # 9. marketing-consulting.html
    # ----------------------------------------------------
    img_mk = register_placeholder(
        "marketing-consulting.html",
        "Practice Hero",
        "marketing-strategy-meeting.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Marketing strategists analyzing customer acquisition funnels and market segmentation data on a digital board.",
        "Corporate marketing advisory team reviewing customer journey flowcharts and brand positioning matrices in a bright modern creative suite. Crisp corporate clothing, engaged expressions, modern technology displays, realistic high-end corporate photography.",
        "Over-the-shoulder medium shot showing clear diagrammatic funnel on display.",
        "Soft diffused natural light combined with warm interior lamps.",
        "Contemporary corporate marketing strategy studio.",
        "Premium editorial commercial photography.",
        "Navy, cobalt blue, warm terracotta accent, white.",
        "Negative space in upper quadrant."
    )

    mk_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Marketing Consulting</li>
        </ul>
        <h1 class="page-hero-title">Strategic Marketing, Brand Positioning, and Acquisition Funnels</h1>
        <p class="page-hero-desc">We help enterprises clarify brand positioning, segment target customer groups, and design disciplined marketing acquisition funnels that convert.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Market Commercialization</span>
            <h2 class="section-title">Moving From Ad-Hoc Marketing to Measurable Customer Acquisition</h2>
            <p class="lead">Marketing without structured positioning and funnel discipline leads to inflated customer acquisition costs and low conversion rates.</p>
            <p>Our marketing consulting practice evaluates target demographics, refines core value propositions, and establishes rigorous marketing funnels and measurement frameworks to maximize return on marketing investments.</p>
          </div>
          <div>{img_mk}</div>
        </div>

        <!-- Visual Marketing Funnel Diagram -->
        <div class="section-header text-center">
          <span class="eyebrow">Funnel Architecture</span>
          <h2 class="section-title">The Four-Stage Strategic Marketing Funnel</h2>
          <p class="section-subtitle">A disciplined progression from brand awareness to sustained customer retention.</p>
        </div>

        <div class="grid-4" style="margin-bottom: 3.5rem;">
          <div class="card" style="border-top: 3px solid #101D35;">
            <div class="eyebrow">Stage 01</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Awareness & Positioning</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Targeted content, brand storytelling, and search visibility to engage pre-qualified enterprise buyers.</p>
          </div>
          <div class="card" style="border-top: 3px solid #244B78;">
            <div class="eyebrow">Stage 02</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Evaluation & Consideration</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Technical whitepapers, demo webinars, and transparent case study walkthroughs to demonstrate capability.</p>
          </div>
          <div class="card" style="border-top: 3px solid #3979C6;">
            <div class="eyebrow">Stage 03</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Decision & Conversion</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Streamlined proposal frameworks, tailored consultative discovery, and clear scope agreements.</p>
          </div>
          <div class="card" style="border-top: 3px solid #B99A5B;">
            <div class="eyebrow">Stage 04</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">Retention & Expansion</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Account review cadences, customer success onboarding, and proactive advisory relationship management.</p>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Brand Positioning & Narrative</h3>
            <p class="card-desc">Differentiating your enterprise from competitors with crisp messaging that speaks directly to executive pain points.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Customer Segmentation</h3>
            <p class="card-desc">Analyzing customer lifetime value (LTV), acquisition cost (CAC), and purchasing behaviors across distinct market segments.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Marketing Metrics & Attribution</h3>
            <p class="card-desc">Implementing analytics architectures that measure channel efficiency and eliminate wasteful advertising spending.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Consult on Marketing Strategy</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "marketing-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Marketing Consulting Practice | Positioning & Funnel Strategy",
            "Marketing strategy, brand positioning, customer segmentation, digital acquisition funnel planning, and performance analysis.",
            "marketing-consulting.html",
            "services",
            mk_body
        ))
    print("Page 9: marketing-consulting.html written.")

    # ----------------------------------------------------
    # 10. it-consulting.html
    # ----------------------------------------------------
    img_it = register_placeholder(
        "it-consulting.html",
        "Practice Hero",
        "it-consulting-architecture.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Enterprise IT consultants evaluating cloud systems architecture and server infrastructure models.",
        "Senior information technology strategy advisors in a modern enterprise server lab or tech control suite examining cloud architecture topology diagrams on large screens. Clean, sophisticated IT environment, realistic and professional.",
        "Three-quarters angle displaying technology diagrams and consultant dialogue.",
        "Balanced cool ambient light with soft blue architectural highlights.",
        "High-tech enterprise operations center.",
        "Modern enterprise commercial photography.",
        "Deep navy, slate grey, steel blue, white.",
        "Clean top space for headline contrast."
    )

    it_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>IT Consulting</li>
        </ul>
        <h1 class="page-hero-title">Enterprise IT Strategy, Architecture, and Systems Advisory</h1>
        <p class="page-hero-desc">We assist organizations in evaluating software architectures, vendor solutions, cloud migration strategies, and IT governance models.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="notice-box notice-info">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Advisory Scope Clarification:</strong> Our IT consulting practice provides strategic management advisory, enterprise software evaluation, and technology roadmapping. We do not perform real-time network intrusion penetration tests, automated vulnerability exploits, or connect to production IT systems through this website demonstration.
          </div>
        </div>

        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Enterprise Technology</span>
            <h2 class="section-title">Aligning Technology Investments With Business Realities</h2>
            <p class="lead">Technology should be an enabler of business velocity, not an unmanageable cost sink or source of operational inertia.</p>
            <p>We provide vendor-neutral assessments of legacy systems, evaluate enterprise software options (ERP, CRM, HRM), review cloud hosting alternatives, and construct pragmatic IT modernization roadmaps.</p>
          </div>
          <div>{img_it}</div>
        </div>

        <!-- Technology Architecture Diagram Mockup -->
        <div class="section-header text-center">
          <span class="eyebrow">Architecture Blueprint</span>
          <h2 class="section-title">Enterprise Systems Assessment Framework</h2>
          <p class="section-subtitle">Evaluating the layers of modern enterprise IT infrastructure.</p>
        </div>

        <div class="grid-3" style="margin-bottom: 3.5rem;">
          <div class="card" style="border-top: 3px solid var(--navy-primary);">
            <div class="eyebrow">Layer 1</div>
            <h3 class="card-title">Core Applications (ERP / CRM)</h3>
            <p class="card-desc">Evaluating feature fit, data normalization, total cost of ownership (TCO), and upgrade paths for transactional business software.</p>
          </div>
          <div class="card" style="border-top: 3px solid var(--blue-accent);">
            <div class="eyebrow">Layer 2</div>
            <h3 class="card-title">Integration & Data Pipes</h3>
            <p class="card-desc">Designing unified API architectures and data pipelines to prevent data silos between sales, finance, and operations.</p>
          </div>
          <div class="card" style="border-top: 3px solid var(--gold-accent);">
            <div class="eyebrow">Layer 3</div>
            <h3 class="card-title">Infrastructure & Cloud Hosting</h3>
            <p class="card-desc">Reviewing cloud migration feasibility, disaster recovery protocols, service level agreements (SLAs), and hosting budgets.</p>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Software Selection Advisory</h3>
            <p class="card-desc">Structured RFP preparation, vendor demonstration scoring, and contractual negotiation guidance for major enterprise software purchases.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Cybersecurity Policy Planning</h3>
            <p class="card-desc">Reviewing data classification policies, access controls, backup regimens, and staff security hygiene protocols.</p>
          </div>
          <div class="card">
            <h3 class="card-title">IT Project Oversight</h3>
            <p class="card-desc">Independent advisory oversight during high-stakes software rollouts to ensure vendor adherence to budget, timeline, and scope.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Discuss Your IT Strategy</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "it-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "IT Consulting Practice | Enterprise Architecture & Strategy",
            "IT consulting services for technology assessment, software selection, enterprise architecture, cloud strategy, and technology project advisory.",
            "it-consulting.html",
            "services",
            it_body
        ))
    print("Page 10: it-consulting.html written.")

    # ----------------------------------------------------
    # 11. digital-transformation.html
    # ----------------------------------------------------
    img_dt = register_placeholder(
        "digital-transformation.html",
        "Practice Hero",
        "digital-transformation-strategy.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Cross-functional team reviewing digital transformation roadmap and automated workflow schematics on interactive screens.",
        "Business leaders and digital transformation consultants collaborating around an interactive digital touchscreen presenting workflow automation maps. Professional office setting, modern architectural lighting, photorealistic commercial photography.",
        "Medium shot showing collaborative interaction with digital roadmap.",
        "Crisp screen illumination balanced with soft warm ambient lighting.",
        "Contemporary digital innovation studio with glass and wood paneling.",
        "Clean, forward-looking corporate commercial style.",
        "Navy, cyan, charcoal, crisp white.",
        "Upper framing open for typography."
    )

    dt_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Digital Transformation</li>
        </ul>
        <h1 class="page-hero-title">Transform Business Processes With the Right Technology Strategy</h1>
        <p class="page-hero-desc">We guide organizations through structured process digitization, workflow automation, cloud adoption, and digital change management.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Process Digitization</span>
            <h2 class="section-title">Pragmatic Digital Modernization Focused on Operational Returns</h2>
            <p class="lead">Digital transformation is not about adopting every emerging tool—it is about systematically eliminating manual bottlenecks, digitizing core handoffs, and improving data access.</p>
            <p>We assess your digital readiness, identify high-impact automation opportunities, and construct a multi-phase digital roadmap that avoids disruptive system overhauls.</p>
          </div>
          <div>{img_dt}</div>
        </div>

        <!-- Digital Transformation Roadmap Diagram -->
        <div class="section-header text-center">
          <span class="eyebrow">Execution Horizon</span>
          <h2 class="section-title">The Four-Phase Digital Transformation Roadmap</h2>
          <p class="section-subtitle">A phased, low-risk approach to modernizing enterprise workflows.</p>
        </div>

        <div class="process-timeline" style="grid-template-columns: repeat(4, 1fr); margin-bottom: 3.5rem;">
          <div class="process-card">
            <span class="process-step-num">Phase 01</span>
            <h3 class="process-card-title">Readiness Assessment</h3>
            <p class="process-card-desc">Auditing manual paper trails, duplicate data entry points, software license utilization, and user adoption barriers.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Phase 02</span>
            <h3 class="process-card-title">Process Digitization</h3>
            <p class="process-card-desc">Redesigning core operational workflows to be digital-first, paperless, and centrally accessible across departments.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Phase 03</span>
            <h3 class="process-card-title">Automation & Cloud</h3>
            <p class="process-card-desc">Connecting key business applications via automated integrations and migrating critical databases to secure cloud environments.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Phase 04</span>
            <h3 class="process-card-title">Change & Culture</h3>
            <p class="process-card-desc">Conducting role-based user training, updating standard operating procedures, and establishing ongoing adoption metrics.</p>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Workflow Automation Scoping</h3>
            <p class="card-desc">Targeting repetitive administrative handoffs suitable for automated routing, notification triggers, and digital approval workflows.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Data-Driven Decision Making</h3>
            <p class="card-desc">Building executive reporting dashboards that surface real-time operational indicators without manual spreadsheet compilation.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Digital Change Governance</h3>
            <p class="card-desc">Structuring transition teams and change champions to overcome staff resistance and ensure full adoption of new digital tools.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Plan Your Digital Transformation</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "digital-transformation.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Digital Transformation Practice | Process Modernization",
            "Digital transformation consulting for process digitization, workflow automation, cloud adoption planning, and digital change management.",
            "digital-transformation.html",
            "services",
            dt_body
        ))
    print("Page 11: digital-transformation.html written.")

    # ----------------------------------------------------
    # 12. operations-consulting.html
    # ----------------------------------------------------
    img_op = register_placeholder(
        "operations-consulting.html",
        "Practice Hero",
        "operations-process-analysis.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Operations consultant conducting workflow analysis and process optimization in a logistics or manufacturing facility.",
        "Industrial operations consultant holding a tablet reviewing supply chain inventory analytics and packaging throughput in a clean, modern distribution center. High level of order and precision, realistic industrial lighting, professional corporate documentary photography.",
        "Medium-wide shot with strong perspective of warehouse distribution lines.",
        "Bright balanced industrial overhead lighting with natural daylight accents.",
        "Pristine logistics hub with organized racking and automated conveyors.",
        "Industrial commercial photography.",
        "Navy, safety amber, cool silver, white.",
        "Upper framing open."
    )

    op_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Operations Consulting</li>
        </ul>
        <h1 class="page-hero-title">Process Optimization, Supply Chain Efficiency, and Quality Control</h1>
        <p class="page-hero-desc">We identify operational bottlenecks, streamline multi-stage workflows, optimize supply chain logistics, and design robust quality management frameworks.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Operational Rigor</span>
            <h2 class="section-title">Eliminating Waste and Restoring Predictability to Core Operations</h2>
            <p class="lead">Operational inefficiencies rarely show up as sudden crises; they accumulate quietly as rework cycles, idle inventory, and misaligned handoffs.</p>
            <p>Our operations consulting practice maps workflows end-to-end, quantifies cycle time variances, and applies Lean and Six Sigma principles to establish predictable, cost-effective operating rhythms.</p>
          </div>
          <div>{img_op}</div>
        </div>

        <!-- Before-and-After Process Flow Illustration -->
        <div class="section-header text-center">
          <span class="eyebrow">Workflow Optimization</span>
          <h2 class="section-title">Illustrative Operational Workflow Redesign</h2>
          <p class="section-subtitle">Visualizing the transition from fragmented legacy handoffs to synchronized operations.</p>
        </div>

        <div class="grid-2" style="margin-bottom: 3.5rem;">
          <div class="card" style="border-left: 4px solid #C5221F;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #C5221F; text-transform: uppercase; margin-bottom: 0.35rem;">Typical Current State: Fragmented Flow</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.75rem;">Siloed Departments & Manual Re-Checks</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary);">Orders pass through disconnected teams with redundant verification steps, paper approvals, and lack of real-time inventory visibility.</p>
            <ul style="font-size: 0.82rem; color: var(--text-secondary); padding-left: 1.25rem;">
              <li>High rework rates due to manual data transpositions</li>
              <li>Extended cycle times waiting for manager sign-offs</li>
              <li>Excess buffer inventory to hedge against stockouts</li>
            </ul>
          </div>

          <div class="card" style="border-left: 4px solid #1E7E34;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #1E7E34; text-transform: uppercase; margin-bottom: 0.35rem;">Target State: Optimized Streamlined Flow</div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.75rem;">Synchronized & Standardized Operations</h4>
            <p style="font-size: 0.88rem; color: var(--text-secondary);">Direct handoffs governed by Standard Operating Procedures (SOPs), automated milestone triggers, and integrated inventory management.</p>
            <ul style="font-size: 0.82rem; color: var(--text-secondary); padding-left: 1.25rem;">
              <li>Predictable turnaround times with standard deviation controls</li>
              <li>Elimination of redundant quality review stations</li>
              <li>Lean working capital allocation across distribution nodes</li>
            </ul>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Process Bottleneck Analysis</h3>
            <p class="card-desc">Time-and-motion studies, queuing analysis, and constraint identification across physical and administrative workflows.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Supply Chain Rationalization</h3>
            <p class="card-desc">Vendor scorecards, safety stock calculations, and logistics route reviews to reduce procurement lead times.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Quality Management SOPs</h3>
            <p class="card-desc">Standardized operating procedures, error-proofing (Poka-Yoke) frameworks, and root cause analysis protocols.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Request an Operational Review</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "operations-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Operations Consulting Practice | Process Optimization & Supply Chain",
            "Operations consulting services for process optimization, workflow analysis, supply chain rationalization, productivity improvements, and quality control.",
            "operations-consulting.html",
            "services",
            op_body
        ))
    print("Page 12: operations-consulting.html written.")

    # ----------------------------------------------------
    # 13. startup-consulting.html
    # ----------------------------------------------------
    img_st = register_placeholder(
        "startup-consulting.html",
        "Practice Hero",
        "startup-business-planning.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Startup founders and advisory consultant mapping product-market fit hypotheses and runway economics on a glass whiteboard.",
        "Two early-stage enterprise founders discussing go-to-market milestones with an experienced business consultant in an agile workspace. Clear strategy framework drawn on glass board, dynamic professional atmosphere, realistic commercial photography.",
        "Medium shot showing consultant and founders reviewing the product validation plan.",
        "Bright natural daylight from industrial loft windows.",
        "Modern incubator or venture advisory studio with brick and glass accents.",
        "Authentic startup corporate photography.",
        "Navy, energetic blue, warm amber, white.",
        "Upper framing open."
    )

    st_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Startup Consulting</li>
        </ul>
        <h1 class="page-hero-title">From Business Idea to a More Structured Startup</h1>
        <p class="page-hero-desc">We help founders and entrepreneurial teams pressure-test business models, structure go-to-market strategies, and build disciplined operational foundations.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="notice-box">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Advisory Disclaimer:</strong> Our startup consulting practice provides business model evaluation, planning frameworks, and operational advisory. We do not offer guaranteed fundraising, broker-dealer securities placements, venture capital investment guarantees, or promises of commercial success. All venture outcomes are subject to market risks.
          </div>
        </div>

        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Early-Stage Strategy</span>
            <h2 class="section-title">Structuring Early-Stage Ventures for Scalable Execution</h2>
            <p class="lead">Great ideas fail when operational mechanics, unit economics, and go-to-market channels are left to chance.</p>
            <p>Our startup consulting practice assists founding teams in testing value propositions, formulating minimum viable product (MVP) roadmaps, defining customer acquisition models, and preparing structured business documentation.</p>
          </div>
          <div>{img_st}</div>
        </div>

        <!-- Startup Growth Roadmap Visualization -->
        <div class="section-header text-center">
          <span class="eyebrow">Venture Roadmap</span>
          <h2 class="section-title">The Four Stages of Startup Maturity</h2>
          <p class="section-subtitle">A structured progression from concept validation to sustainable commercial growth.</p>
        </div>

        <div class="process-timeline" style="grid-template-columns: repeat(4, 1fr); margin-bottom: 3.5rem;">
          <div class="process-card">
            <span class="process-step-num">Stage 01</span>
            <h3 class="process-card-title">Concept & Hypotheses</h3>
            <p class="process-card-desc">Defining target customer segments, testing problem-solution fit, and analyzing competitor pricing models.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 02</span>
            <h3 class="process-card-title">Model Validation</h3>
            <p class="process-card-desc">Scoping MVP functionality, determining unit economics (CAC, LTV), and validating willingness-to-pay.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 03</span>
            <h3 class="process-card-title">Go-to-Market Design</h3>
            <p class="process-card-desc">Establishing repeatable sales funnels, distribution partnerships, customer onboarding journeys, and support SLAs.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 04</span>
            <h3 class="process-card-title">Operational Scale</h3>
            <p class="process-card-desc">Structuring reporting lines, cash runway monitoring, and formalizing standard operating procedures for team growth.</p>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Unit Economics Modeling</h3>
            <p class="card-desc">Detailed spreadsheet modeling of customer acquisition costs, churn projections, gross margins, and burn rates.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Pitch Deck Preparation</h3>
            <p class="card-desc">Refining problem statements, market size estimations, traction milestones, and financial summaries for stakeholder presentations.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Operating Foundations</h3>
            <p class="card-desc">Setting up foundational governance, contractor agreements, intellectual property assignments, and compliance calendars.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Schedule a Startup Advisory Session</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "startup-consulting.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Startup Consulting Practice | Business Planning & Scaling",
            "Startup consulting services for business model validation, MVP scoping, go-to-market strategy, unit economics, and operational scaling.",
            "startup-consulting.html",
            "services",
            st_body
        ))
    print("Page 13: startup-consulting.html written.")

    # ----------------------------------------------------
    # 14. risk-management.html
    # ----------------------------------------------------
    img_rm = register_placeholder(
        "risk-management.html",
        "Practice Hero",
        "risk-management-framework.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Enterprise risk advisory team evaluating risk heatmaps and business continuity contingencies in an executive boardroom.",
        "Corporate risk advisors and executive officers reviewing an enterprise risk matrix and scenario impact analysis on a large conference screen. High level of focus, refined business suits, corporate boardroom with elegant wood finishes, photorealistic commercial photography.",
        "Medium-wide shot showing the risk matrix on display and executive dialogue.",
        "Soft recessed architectural downlights with daylight window fill.",
        "Refined corporate boardroom overlooking commercial district.",
        "Corporate editorial commercial style.",
        "Deep navy, slate grey, alert amber, clean white.",
        "Clean top area for title legibility."
    )

    rm_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Risk Management</li>
        </ul>
        <h1 class="page-hero-title">Business Risk Identification, Assessment, and Continuity Planning</h1>
        <p class="page-hero-desc">We assist executive teams in identifying operational vulnerabilities, designing risk mitigation matrices, and formulating resilient business continuity plans.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="notice-box">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          <div class="notice-content">
            <strong>Advisory Scope & Legal Disclaimer:</strong> The risk advisory capabilities presented on this website represent general management consulting frameworks for operational resilience. This firm does not provide formal legal counsel, statutory regulatory audit certifications, insurance underwriting, or actuarial underwriting services.
          </div>
        </div>

        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Enterprise Resilience</span>
            <h2 class="section-title">Protecting Enterprise Value Through Proactive Risk Governance</h2>
            <p class="lead">Organizations that fail to catalog and quantify operational risks are vulnerable to compounding disruptions when external shocks occur.</p>
            <p>Our risk management practice assists leadership in mapping single points of failure across supply chains, personnel, regulatory compliance, and technology systems—establishing clear mitigation actions before disruptions occur.</p>
          </div>
          <div>{img_rm}</div>
        </div>

        <!-- Illustrative 5x5 Risk Matrix Component -->
        <div class="section-header text-center">
          <span class="eyebrow">Diagnostic Matrix</span>
          <h2 class="section-title">Illustrative Enterprise Risk Matrix</h2>
          <p class="section-subtitle">A standard 5x5 likelihood-versus-impact risk classification model.</p>
        </div>

        <div style="overflow-x: auto; margin-bottom: 3.5rem;">
          <table class="risk-matrix-table">
            <thead>
              <tr>
                <th style="width: 20%;">Likelihood / Impact</th>
                <th style="width: 16%;">1 - Negligible</th>
                <th style="width: 16%;">2 - Minor</th>
                <th style="width: 16%;">3 - Moderate</th>
                <th style="width: 16%;">4 - Major</th>
                <th style="width: 16%;">5 - Critical</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th>5 - Almost Certain</th>
                <td class="risk-med">Medium (5)</td>
                <td class="risk-med">Medium (10)</td>
                <td class="risk-high">High (15)</td>
                <td class="risk-high">High (20)</td>
                <td class="risk-high">Severe (25)</td>
              </tr>
              <tr>
                <th>4 - Likely</th>
                <td class="risk-low">Low (4)</td>
                <td class="risk-med">Medium (8)</td>
                <td class="risk-med">Medium (12)</td>
                <td class="risk-high">High (16)</td>
                <td class="risk-high">Severe (20)</td>
              </tr>
              <tr>
                <th>3 - Possible</th>
                <td class="risk-low">Low (3)</td>
                <td class="risk-low">Low (6)</td>
                <td class="risk-med">Medium (9)</td>
                <td class="risk-high">High (12)</td>
                <td class="risk-high">High (15)</td>
              </tr>
              <tr>
                <th>2 - Unlikely</th>
                <td class="risk-low">Low (2)</td>
                <td class="risk-low">Low (4)</td>
                <td class="risk-low">Low (6)</td>
                <td class="risk-med">Medium (8)</td>
                <td class="risk-med">Medium (10)</td>
              </tr>
              <tr>
                <th>1 - Rare</th>
                <td class="risk-low">Low (1)</td>
                <td class="risk-low">Low (2)</td>
                <td class="risk-low">Low (3)</td>
                <td class="risk-low">Low (4)</td>
                <td class="risk-med">Medium (5)</td>
              </tr>
            </tbody>
          </table>
          <div style="font-size: 0.75rem; color: var(--text-muted); text-align: center; margin-top: 0.5rem;">
            * Illustrative Risk Classification Matrix for Diagnostic Prioritization
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Operational Risk Review</h3>
            <p class="card-desc">Reviewing key vendor dependencies, warehouse single points of failure, and operational safety compliance procedures.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Business Continuity Planning (BCP)</h3>
            <p class="card-desc">Formulating incident command hierarchies, communication protocols, and backup facility arrangements for crisis response.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Internal Controls Assessment</h3>
            <p class="card-desc">Evaluating separation of duties, expenditure authorization limits, and inventory reconciliation mechanisms.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Request Risk Assessment Advisory</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "risk-management.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Risk Management Practice | Enterprise Continuity & Risk Matrices",
            "Risk management consulting services for operational risk identification, risk matrix modeling, internal process reviews, and business continuity planning.",
            "risk-management.html",
            "services",
            rm_body
        ))
    print("Page 14: risk-management.html written.")

    # ----------------------------------------------------
    # 15. project-management.html
    # ----------------------------------------------------
    img_pm = register_placeholder(
        "project-management.html",
        "Practice Hero",
        "project-management-governance.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Project management consultants tracking multi-stage enterprise deliverables, Gantt milestones, and risk logs in a project war room.",
        "Project delivery consultants reviewing critical path schedules, resource allocation tables, and milestone burn-down charts in a contemporary project steering office. Highly professional demeanor, crisp business suits, realistic commercial photography.",
        "Medium-wide shot with clear view of project schedules and steering team.",
        "Bright natural light with crisp screen glow.",
        "Modern corporate project governance war room.",
        "Corporate project management commercial photography.",
        "Navy, slate blue, warm brass, white.",
        "Upper framing open."
    )

    pm_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Project Management</li>
        </ul>
        <h1 class="page-hero-title">Project Governance, Scope Definition, and Delivery Coordination</h1>
        <p class="page-hero-desc">We establish Project Management Offices (PMOs), structure delivery governance, track critical-path timelines, and manage execution risk across complex business initiatives.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Delivery Governance</span>
            <h2 class="section-title">Bringing Predictability and Discipline to Complex Strategic Initiatives</h2>
            <p class="lead">Even well-funded initiatives fail when cross-functional dependencies are unmanaged, scope creep goes unchecked, and milestone accountability is diffuse.</p>
            <p>Our project management advisory practice establishes formal PMO charters, schedules realistic milestone timelines, implements risk and issue logs (RAID), and provides steering committee transparency.</p>
          </div>
          <div>{img_pm}</div>
        </div>

        <!-- Illustrative Project Timeline and Dashboard Mockup -->
        <div class="dashboard-preview" style="margin-bottom: 3.5rem;">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Enterprise Project Steering & Milestone Tracker Mockup</h4>
              <span>Critical Path Governance &bull; Demo PMO Architecture</span>
            </div>
            <span class="demo-pill">Illustrative Demo Data</span>
          </div>

          <div class="dashboard-metrics-grid">
            <div class="metric-box">
              <div class="metric-label">Milestone Schedule Variance</div>
              <div class="metric-value">+2.5 Days</div>
              <div class="metric-trend">&bull; Controlled Variance Threshold</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Scope Change Requests</div>
              <div class="metric-value">4 Approved</div>
              <div class="metric-trend">&uarr; Fully Baselined</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Critical Path Adherence</div>
              <div class="metric-value">94.8%</div>
              <div class="metric-trend">&bull; High Delivery Confidence</div>
            </div>
          </div>

          <div class="chart-container">
            <div class="chart-title">
              <span>Execution Phases & Milestone Status</span>
              <span style="font-size: 0.72rem; color: #8E9BAE;">Phased Workstreams</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.75rem; padding-top: 0.5rem;">
              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                  <span>Phase 1: Project Charter & Scope Baseline</span>
                  <span style="color: #38C172;">Completed (100%)</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                  <div style="background: #38C172; width: 100%; height: 100%;"></div>
                </div>
              </div>
              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                  <span>Phase 2: Detailed Workflow Blueprinting</span>
                  <span style="color: var(--blue-accent);">In Progress (85%)</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                  <div style="background: var(--blue-accent); width: 85%; height: 100%;"></div>
                </div>
              </div>
              <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                  <span>Phase 3: Operational Pilot & Verification</span>
                  <span style="color: var(--gold-accent);">Scheduled (30%)</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                  <div style="background: var(--gold-accent); width: 30%; height: 100%;"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h3 class="card-title">Scope & Baseline Management</h3>
            <p class="card-desc">Establishing Work Breakdown Structures (WBS) and formal change control mechanisms to prevent unauthorized scope creep.</p>
          </div>
          <div class="card">
            <h3 class="card-title">RAID Log & Risk Oversight</h3>
            <p class="card-desc">Proactive management of Risks, Assumptions, Issues, and Dependencies to mitigate delivery roadblocks before they impact milestones.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Steering Committee Reporting</h3>
            <p class="card-desc">Executive dash-cards communicating budget burn, milestone variances, and high-level decisions requiring leadership intervention.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Consult on Project Governance</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "project-management.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Project Management Practice | Governance & Delivery Oversight",
            "Project management consulting services for PMO setup, scope baseline management, timeline tracking, resource coordination, and delivery governance.",
            "project-management.html",
            "services",
            pm_body
        ))
    print("Page 15: project-management.html written.")

    # ----------------------------------------------------
    # 16. organizational-development.html
    # ----------------------------------------------------
    img_od = register_placeholder(
        "organizational-development.html",
        "Practice Hero",
        "organizational-development-culture.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Organizational development advisors facilitating a leadership alignment and cultural transformation workshop.",
        "Organizational development consultants guiding an executive management workshop around circular team alignment and culture models. Engaged leadership participants, bright contemporary architectural space, warm natural light, realistic corporate photography.",
        "Medium shot capturing the collaborative dynamic between consultants and leadership.",
        "Bright natural window light with gentle ambient warmth.",
        "Contemporary executive leadership training retreat space.",
        "Authentic corporate leadership photography.",
        "Deep navy, warm ochre, soft grey, clean white.",
        "Upper framing open."
    )

    od_body = f'''
    <section class="page-hero">
      <div class="container">
        <ul class="breadcrumb">
          <li><a href="index.html">Home</a></li>
          <li class="breadcrumb-separator">/</li>
          <li><a href="services.html">Services</a></li>
          <li class="breadcrumb-separator">/</li>
          <li>Organizational Development</li>
        </ul>
        <h1 class="page-hero-title">Organizational Alignment, Performance Culture, and Leadership Growth</h1>
        <p class="page-hero-desc">We help organizations align workforce behaviors, evolve corporate culture, and structure leadership frameworks that sustain high performance through business transitions.</p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="grid-2" style="align-items: center; margin-bottom: 4rem;">
          <div>
            <span class="eyebrow">Culture & Alignment</span>
            <h2 class="section-title">Building Resilient Organizational Capabilities From Within</h2>
            <p class="lead">Strategic pivots and technology rollouts only succeed when the underlying human system—habits, incentives, leadership behaviors, and cross-functional communication—is intentionally aligned.</p>
            <p>Our organizational development practice diagnoses cultural friction points, designs leadership development frameworks, and implements change management roadmaps that ensure strategic goals become operational realities.</p>
          </div>
          <div>{img_od}</div>
        </div>

        <div class="section-header text-center">
          <span class="eyebrow">Transformation Dimensions</span>
          <h2 class="section-title">The Four Pillars of Organizational Development</h2>
          <p class="section-subtitle">A holistic approach to enterprise capability building.</p>
        </div>

        <div class="grid-4" style="margin-bottom: 3.5rem;">
          <div class="card" style="border-top: 3px solid var(--navy-primary);">
            <div class="card-icon" style="background: var(--blue-subtle);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">1. Team Effectiveness</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Breaking down departmental silos, clarifying shared incentives, and streamlining cross-functional handoffs.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--blue-secondary);">
            <div class="card-icon" style="background: var(--blue-subtle); color: var(--blue-secondary);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">2. Leadership Cadence</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Equipping mid-level and senior managers with structured coaching, feedback models, and delegation competencies.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--blue-accent);">
            <div class="card-icon" style="background: var(--blue-light); color: var(--blue-accent);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">3. Performance Culture</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Fostering psychological safety balanced with unyielding accountability and transparent outcome tracking.</p>
          </div>

          <div class="card" style="border-top: 3px solid var(--gold-accent);">
            <div class="card-icon" style="background: var(--gold-light); color: var(--gold-accent);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </div>
            <h4 style="color: var(--navy-primary); margin-bottom: 0.5rem;">4. Change Resilience</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Establishing feedback channels and transition rituals that prevent staff burnout during organizational restructuring.</p>
          </div>
        </div>

        <div class="grid-2">
          <div class="card">
            <h3 class="card-title">Cultural Assessment & Diagnostic</h3>
            <p class="card-desc">Anonymous organizational pulse surveys, managerial interviews, and behavioral audits to identify friction points and misaligned incentives.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Leadership Alignment Workshops</h3>
            <p class="card-desc">Facilitated executive off-sites dedicated to resolving interpersonal conflict, clarifying shared mandates, and unifying leadership language.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="book-consultation.html" class="btn btn-primary btn-lg">Consult on Organizational Development</a>
        </div>
      </div>
    </section>
    '''

    with open(os.path.join(BASE_DIR, "organizational-development.html"), "w", encoding="utf-8") as f:
        f.write(get_page_shell(
            "Organizational Development Practice | Culture & Leadership",
            "Organizational development consulting for cultural assessment, leadership alignment, team effectiveness, change enablement, and performance culture.",
            "organizational-development.html",
            "services",
            od_body
        ))
    print("Page 16: organizational-development.html written.")

generate_individual_services()
