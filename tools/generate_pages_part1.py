import os
import json
from build_helpers import get_page_shell, make_placeholder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Global inventory of image placeholders:
# key: filename, value: dict with metadata and prompt info
IMAGE_INVENTORY = []

def register_placeholder(page_file, section, filename, aspect, dimensions, orientation, subject_desc, prompt, comp, lighting, bg, style, palette, negative_space):
    placeholder_markup = make_placeholder(filename, aspect, dimensions, subject_desc)
    IMAGE_INVENTORY.append({
        "number": len(IMAGE_INVENTORY) + 1,
        "filename": filename,
        "page": page_file,
        "section": section,
        "subject_desc": subject_desc,
        "aspect_ratio": aspect.replace("aspect-", "").replace("-", ":"),
        "dimensions": dimensions,
        "orientation": orientation,
        "prompt": prompt,
        "composition": comp,
        "lighting": lighting,
        "background": bg,
        "visual_style": style,
        "palette": palette,
        "negative_space": negative_space
    })
    return placeholder_markup

# ==========================================
# PAGE 1: index.html (Homepage)
# ==========================================
def build_index():
    hero_img = register_placeholder(
        "index.html",
        "Homepage Hero",
        "hero-business-consulting.webp",
        "aspect-16-9",
        "1920x1080",
        "Landscape",
        "Modern corporate strategic advisory meeting in a high-rise executive boardroom with executive decision-makers reviewing business roadmap graphics on a glass board.",
        "High-end corporate photography of a modern executive boardroom overlooking a city skyline. A diverse group of professional business consultants and executives in tailored business suits engaged in a strategic discussion around a dark walnut table. A sleek glass whiteboard with subtle strategic frameworks and timeline charts. Natural daylight through large floor-to-ceiling windows, subtle navy and brass interior accents, sophisticated and calm atmosphere, ultra-sharp focus, cinematic depth of field, photorealistic 8k.",
        "Medium-wide shot with clear focal point on executives and table framework; elegant perspective lines.",
        "Soft diffused morning daylight through panoramic windows with warm subtle interior architectural lighting.",
        "Modern high-rise executive suite with floor-to-ceiling glass and distant city architecture.",
        "Premium editorial corporate photography, dignified and understated, Hasselblad medium format look.",
        "Deep corporate navy, warm walnut timber, crisp slate grey, subtle gold brass accents.",
        "Ample upper and side space for crisp UI framing."
    )

    approach_img = register_placeholder(
        "index.html",
        "Consulting Approach Overview",
        "consulting-methodology-preview.webp",
        "aspect-16-9",
        "1280x720",
        "Landscape",
        "Senior business analyst mapping operational workflows and growth phases on a glass planning wall.",
        "Professional business advisor pointing towards an analytical process flow diagram on an architectural glass panel in a contemporary office. Focused expression, sharp corporate attire, minimalist architectural background with balanced depth. High-end commercial photography, crisp details, natural color balance.",
        "Medium shot showing consultant in three-quarters profile gesturing toward clear diagram.",
        "Balanced cool daylight with soft warm downlighting.",
        "Glass-partitioned enterprise innovation hub with soft bokeh.",
        "Clean corporate documentary style, professional and authentic.",
        "Corporate navy, white frosted glass, subtle deep blue and neutral greys.",
        "Negative space on the right side of the frame."
    )

    case_preview_img1 = register_placeholder(
        "index.html",
        "Featured Case Studies - Manufacturing",
        "case-study-operational-excellence.webp",
        "aspect-16-9",
        "800x450",
        "Landscape",
        "Operations consultant inspecting automated production line and logistics workflow in a modern manufacturing facility.",
        "Operations management consultant in high-visibility safety vest and clean corporate business attire standing beside advanced manufacturing engineering equipment. Holding an industrial tablet displaying workflow metrics. Industrial engineering context, clean factory floor, sharp focus, realistic commercial photography.",
        "Rule of thirds composition, consultant on left, industrial line leading back into depth.",
        "Even industrial illumination with soft ambient fill.",
        "Pristine modern manufacturing facility with robotic automated arms.",
        "Industrial enterprise corporate photography, authentic and grounded.",
        "Steel grey, industrial navy blue, safety yellow accent, cool white.",
        "Clean top area for title card overlay."
    )

    case_preview_img2 = register_placeholder(
        "index.html",
        "Featured Case Studies - Technology",
        "case-study-digital-transformation.webp",
        "aspect-16-9",
        "800x450",
        "Landscape",
        "Technology consulting team reviewing digital systems architecture on modern displays.",
        "A focused enterprise technology strategy team analyzing systems infrastructure models in a contemporary tech lab. Two professionals collaborating over interactive dual displays showing architecture diagrams. Sharp modern office aesthetic, photorealistic editorial photography.",
        "Over-the-shoulder medium shot showing screens and collaborative focus.",
        "Cool balanced monitor glow combined with soft warm ceiling LED cove lights.",
        "Minimalist tech advisory office with glass doors and wood slat accent walls.",
        "Modern enterprise technology photo, crisp and credible.",
        "Deep navy, slate blue, neutral white, muted teal accents.",
        "Upper third open for clear UI spacing."
    )

    body = f'''
    <!-- Hero Section -->
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-content">
          <div class="eyebrow">Enterprise Strategic Advisory</div>
          <h1 class="hero-title">MAKE BETTER BUSINESS DECISIONS. BUILD WHAT COMES NEXT.</h1>
          <p class="hero-desc">Practical consulting, strategic thinking, and business-focused solutions to help organizations move forward with clarity and confidence.</p>
          <div class="hero-actions">
            <a href="book-consultation.html" class="btn btn-primary btn-lg">Book a Consultation</a>
            <a href="services.html" class="btn btn-secondary btn-lg">Explore Our Services</a>
          </div>
          <div class="hero-trust-bar">
            <span class="trust-label">Consulting Focus Areas</span>
            <div class="trust-badges">
              <span class="trust-badge-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Strategic Direction
              </span>
              <span class="trust-badge-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Operational Efficiency
              </span>
              <span class="trust-badge-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Organizational Structure
              </span>
              <span class="trust-badge-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Technology Planning
              </span>
            </div>
          </div>
        </div>
        <div class="hero-visual">
          {hero_img}
        </div>
      </div>
    </section>

    <!-- Services Overview Section -->
    <section class="section bg-white">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Core Practice Areas</span>
          <h2 class="section-title">Consulting Services Built for Enterprise Challenges</h2>
          <p class="section-subtitle">We partner with organizations to address core strategic, organizational, and technological priorities through disciplined advisory engagements.</p>
        </div>

        <div class="grid-3">
          <div class="card hover-lift">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
            </div>
            <h3 class="card-title">Business Consulting</h3>
            <p class="card-desc">Practical business planning, business model evaluation, and operational reviews to structure organizations for measured growth.</p>
            <div class="card-footer">
              <a href="business-consulting.html" style="font-weight: 600;">Explore Practice &rarr;</a>
              <span class="demo-pill" style="font-size: 0.68rem;">Strategic</span>
            </div>
          </div>

          <div class="card hover-lift">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            </div>
            <h3 class="card-title">Strategy Consulting</h3>
            <p class="card-desc">Turn market opportunities and executive ambitions into clear, actionable corporate strategies with structured execution roadmaps.</p>
            <div class="card-footer">
              <a href="strategy-consulting.html" style="font-weight: 600;">Explore Practice &rarr;</a>
              <span class="demo-pill" style="font-size: 0.68rem;">Advisory</span>
            </div>
          </div>

          <div class="card hover-lift">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
            </div>
            <h3 class="card-title">Financial Consulting</h3>
            <p class="card-desc">Financial modeling, performance diagnostics, cost structure reviews, and cash flow planning to support sound commercial choices.</p>
            <div class="card-footer">
              <a href="financial-consulting.html" style="font-weight: 600;">Explore Practice &rarr;</a>
              <span class="demo-pill" style="font-size: 0.68rem;">Commercial</span>
            </div>
          </div>

          <div class="card hover-lift">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            </div>
            <h3 class="card-title">Management Consulting</h3>
            <p class="card-desc">Enhance governance frameworks, decision-making processes, leadership alignment, and organizational operating efficiency.</p>
            <div class="card-footer">
              <a href="management-consulting.html" style="font-weight: 600;">Explore Practice &rarr;</a>
              <span class="demo-pill" style="font-size: 0.68rem;">Governance</span>
            </div>
          </div>

          <div class="card hover-lift">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            </div>
            <h3 class="card-title">Digital Transformation</h3>
            <p class="card-desc">Modernize manual workflows, evaluate technology stacks, and execute digital roadmaps that yield sustainable operational returns.</p>
            <div class="card-footer">
              <a href="digital-transformation.html" style="font-weight: 600;">Explore Practice &rarr;</a>
              <span class="demo-pill" style="font-size: 0.68rem;">Technology</span>
            </div>
          </div>

          <div class="card hover-lift">
            <div class="card-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
            </div>
            <h3 class="card-title">Operations Consulting</h3>
            <p class="card-desc">Identify operational bottlenecks, optimize supply chains, streamline workflows, and enhance quality control frameworks.</p>
            <div class="card-footer">
              <a href="operations-consulting.html" style="font-weight: 600;">Explore Practice &rarr;</a>
              <span class="demo-pill" style="font-size: 0.68rem;">Operations</span>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3rem;">
          <a href="services.html" class="btn btn-secondary">View All 13 Consulting Services &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Business Challenges We Solve -->
    <section class="section bg-light-blue">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Strategic Interventions</span>
          <h2 class="section-title">Critical Business Challenges We Address</h2>
          <p class="section-subtitle">Leadership teams engage our advisory capabilities when navigating pivotal turning points and structural operational friction.</p>
        </div>

        <div class="grid-2">
          <div class="card">
            <h3 style="font-size: 1.3rem; margin-bottom: 0.75rem; color: var(--navy-primary);">Slowing Growth & Market Stagnation</h3>
            <p>When core service offerings or products face plateauing revenues, we analyze customer segmentation, competitive positioning, and unexplored market channels to formulate realistic growth strategies.</p>
            <ul style="padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary);">
              <li>Addressable market assessment</li>
              <li>Competitive differentiation analysis</li>
              <li>New revenue stream feasibility review</li>
            </ul>
          </div>

          <div class="card">
            <h3 style="font-size: 1.3rem; margin-bottom: 0.75rem; color: var(--navy-primary);">Operational Complexity & Cost Inefficiencies</h3>
            <p>Rapid expansion frequently creates redundant workflows and departmental silos. We map operational handoffs, evaluate overhead allocations, and design lean operating models.</p>
            <ul style="padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary);">
              <li>End-to-end process mapping</li>
              <li>Cost allocation & variance diagnostics</li>
              <li>Workflow automation recommendations</li>
            </ul>
          </div>

          <div class="card">
            <h3 style="font-size: 1.3rem; margin-bottom: 0.75rem; color: var(--navy-primary);">Organizational Realignment & Leadership Friction</h3>
            <p>Misaligned reporting structures and vague accountability undermine strategic execution. We design clear organizational charts, accountability matrices, and decision frameworks.</p>
            <ul style="padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary);">
              <li>RACI decision-rights matrices</li>
              <li>Organizational restructuring plans</li>
              <li>Performance management frameworks</li>
            </ul>
          </div>

          <div class="card">
            <h3 style="font-size: 1.3rem; margin-bottom: 0.75rem; color: var(--navy-primary);">Legacy Systems & Digital Fragmentation</h3>
            <p>Disconnected software tools and manual reconciliation slow down business cycles. We assess IT architectures and build phased digital transformation roadmaps.</p>
            <ul style="padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-secondary);">
              <li>Digital readiness and gap analysis</li>
              <li>Software vendor evaluation</li>
              <li>Phased rollout & change governance</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- CSS Dashboard Preview Component: Business Performance Dashboard -->
    <section class="section bg-white">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Analytical Precision</span>
          <h2 class="section-title">Data-Driven Consulting Intelligence</h2>
          <p class="section-subtitle">Our recommendations rest on thorough business diagnostics, clear performance indicators, and structural modeling.</p>
        </div>

        <div class="dashboard-preview">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Enterprise Performance Diagnostics Mockup</h4>
              <span>Illustrative Consulting Framework &bull; Demo Analytics Representation</span>
            </div>
            <span class="demo-pill">Illustrative Demo Data</span>
          </div>

          <div class="dashboard-metrics-grid">
            <div class="metric-box">
              <div class="metric-label">Operating Margin Indicator</div>
              <div class="metric-value">24.8%</div>
              <div class="metric-trend">&uarr; Normalized Benchmark Target</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Process Cycle Time</div>
              <div class="metric-value">14.2 Days</div>
              <div class="metric-trend">&darr; Target Efficiency Variance</div>
            </div>
            <div class="metric-box">
              <div class="metric-label">Resource Utilization</div>
              <div class="metric-value">88.5%</div>
              <div class="metric-trend">&bull; Balanced Capacity Tier</div>
            </div>
          </div>

          <div class="grid-2">
            <div class="chart-container">
              <div class="chart-title">
                <span>Revenue Variance by Strategic Segment</span>
                <span style="font-size: 0.72rem; color: #8E9BAE;">Indexed Scale</span>
              </div>
              <div class="bar-chart-mock">
                <div class="bar-col">
                  <div class="bar-fill" style="height: 45%;"></div>
                  <span class="bar-label">Q1 Base</span>
                </div>
                <div class="bar-col">
                  <div class="bar-fill" style="height: 60%;"></div>
                  <span class="bar-label">Q2 Adj</span>
                </div>
                <div class="bar-col">
                  <div class="bar-fill gold" style="height: 80%;"></div>
                  <span class="bar-label">Q3 Opt</span>
                </div>
                <div class="bar-col">
                  <div class="bar-fill gold" style="height: 95%;"></div>
                  <span class="bar-label">Q4 Proj</span>
                </div>
              </div>
            </div>

            <div class="chart-container">
              <div class="chart-title">
                <span>Expense Category Rationalization</span>
                <span style="font-size: 0.72rem; color: #8E9BAE;">Functional Cost Centers</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 0.65rem; padding-top: 0.5rem;">
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>Direct Operational Delivery</span>
                    <span>42%</span>
                  </div>
                  <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: var(--blue-accent); width: 42%; height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>Administrative & Governance Overhead</span>
                    <span>28%</span>
                  </div>
                  <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: var(--gold-accent); width: 28%; height: 100%;"></div>
                  </div>
                </div>
                <div>
                  <div style="display: flex; justify-content: space-between; font-size: 0.75rem; margin-bottom: 0.25rem;">
                    <span>Technology & Infrastructure</span>
                    <span>18%</span>
                  </div>
                  <div style="background: rgba(255,255,255,0.08); height: 6px; border-radius: 3px; overflow: hidden;">
                    <div style="background: #38C172; width: 18%; height: 100%;"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Consulting Methodology Section -->
    <section class="section bg-light-blue">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Structured Execution</span>
          <h2 class="section-title">Our Consulting Approach</h2>
          <p class="section-subtitle">A disciplined five-stage advisory model designed to maintain clarity from initial inquiry through execution support.</p>
        </div>

        <div class="process-timeline">
          <div class="process-card">
            <span class="process-step-num">Stage 01</span>
            <h3 class="process-card-title">Discover</h3>
            <p class="process-card-desc">Comprehensive stakeholder interviews, business model orientation, and definition of strategic boundaries.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 02</span>
            <h3 class="process-card-title">Assess</h3>
            <p class="process-card-desc">Review of current workflows, operational metrics, financial reporting lines, and organizational bottlenecks.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 03</span>
            <h3 class="process-card-title">Analyze</h3>
            <p class="process-card-desc">Rigorous diagnostic evaluation of underlying root causes, scenario planning, and strategic options.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 04</span>
            <h3 class="process-card-title">Recommend</h3>
            <p class="process-card-desc">Formulation of actionable consulting roadmaps, priority matrices, and resource allocation models.</p>
          </div>
          <div class="process-card">
            <span class="process-step-num">Stage 05</span>
            <h3 class="process-card-title">Support</h3>
            <p class="process-card-desc">Advisory support during implementation checkpoints, review cadence, and governance alignment.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2.5rem;">
          <a href="methodology.html" class="btn btn-secondary">Learn More About Our Methodology &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Featured Illustrative Case Studies -->
    <section class="section bg-white">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Demonstration Case Studies</span>
          <h2 class="section-title">Illustrative Advisory Engagements</h2>
          <p class="section-subtitle">Examine simulated consulting engagements illustrating our problem-solving methodology across industries.</p>
        </div>

        <div class="notice-box notice-info" style="margin-bottom: 2.5rem;">
          <svg class="notice-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          <div class="notice-content">
            <strong>Illustrative Demo Notice:</strong> The case studies below represent hypothetical demonstration scenarios created to showcase consulting methodology, diagnostic frameworks, and deliverable structures. They do not represent real client engagements, actual corporate results, or verified commercial figures.
          </div>
        </div>

        <div class="grid-2">
          <div class="card hover-lift">
            <div style="margin-bottom: 1.25rem;">
              {case_preview_img1}
            </div>
            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
              <span class="demo-pill" style="font-size: 0.7rem;">Manufacturing</span>
              <span class="demo-pill" style="font-size: 0.7rem; background: var(--blue-light); border-color: var(--blue-accent); color: var(--navy-primary);">Operational Process Review Demo</span>
            </div>
            <h3 class="card-title">Multi-Plant Operational Flow & Capacity Planning</h3>
            <p class="card-desc">Illustrative advisory engagement addressing throughput bottlenecks and inter-facility inventory distribution challenges across regional plants.</p>
            <div class="card-footer">
              <a href="case-study-details.html" style="font-weight: 600;">Read Illustrative Case Study &rarr;</a>
              <span style="font-size: 0.8rem; color: var(--text-muted);">6 Min Read</span>
            </div>
          </div>

          <div class="card hover-lift">
            <div style="margin-bottom: 1.25rem;">
              {case_preview_img2}
            </div>
            <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
              <span class="demo-pill" style="font-size: 0.7rem;">Technology</span>
              <span class="demo-pill" style="font-size: 0.7rem; background: var(--blue-light); border-color: var(--blue-accent); color: var(--navy-primary);">Digital Transformation Demo</span>
            </div>
            <h3 class="card-title">Enterprise Systems Consolidation & Cloud Architecture</h3>
            <p class="card-desc">Demonstration engagement examining legacy software retirement, centralized data governance, and phased ERP modernization roadmaps.</p>
            <div class="card-footer">
              <a href="case-study-details.html" style="font-weight: 600;">Read Illustrative Case Study &rarr;</a>
              <span style="font-size: 0.8rem; color: var(--text-muted);">5 Min Read</span>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3rem;">
          <a href="case-studies.html" class="btn btn-secondary">Explore All Case Study Demos &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="section bg-navy" style="text-align: center;">
      <div class="container container-narrow">
        <span class="eyebrow eyebrow-gold">Initiate an Advisory Discussion</span>
        <h2 style="color: #FFF; font-size: 2.4rem; margin-bottom: 1.25rem;">Ready to Clarify Your Strategic Priorities?</h2>
        <p style="color: #C0CFE2; font-size: 1.15rem; margin-bottom: 2rem;">Schedule an exploratory consultation with our business advisors. We discuss your business model, current obstacles, and potential consulting roadmaps.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Schedule Consultation</a>
          <a href="contact.html" class="btn btn-secondary btn-lg" style="color: #FFF; border-color: rgba(255,255,255,0.3);">General Enquiry</a>
        </div>
      </div>
    </section>
    '''

    html = get_page_shell(
        "Clarity for Better Decisions. Strategy for Sustainable Growth.",
        "Practical business consulting, strategic advisory, operational improvement, and organizational development to help businesses navigate challenges and grow.",
        "index.html",
        "home",
        body
    )

    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Page 1: index.html written.")

build_index()
