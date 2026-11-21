/**
 * CONSULTING COMPANY — FORMS SCRIPT
 * Multi-Step Consultation Wizard, Contact Form Validation, Careers Submission
 * Note: Demonstration static environment — No data is transmitted or stored.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Helper: Display demo modal/banner
  const showDemoNotice = (title, message) => {
    let existingModal = document.getElementById('demo-response-modal');
    if (existingModal) existingModal.remove();

    const modalHTML = `
      <div id="demo-response-modal" style="position: fixed; inset: 0; background: rgba(10, 20, 38, 0.7); display: flex; align-items: center; justify-content: center; z-index: 10000; padding: 1.5rem;">
        <div style="background: #FFFFFF; border-radius: 8px; max-width: 500px; width: 100%; padding: 2.25rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3); text-align: center; border: 1px solid #E1E7EF;">
          <div style="width: 52px; height: 52px; background: #EAF7ED; color: #1E7E34; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.25rem;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <h3 style="color: #0A1426; font-size: 1.35rem; margin-bottom: 0.75rem;">${title}</h3>
          <p style="color: #667085; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">${message}</p>
          <div style="background: #FEF9EB; border: 1px solid #EBD599; border-radius: 4px; padding: 0.75rem; margin-bottom: 1.5rem; font-size: 0.8rem; color: #7A5300; text-align: left;">
            <strong>Demonstration Notice:</strong> This website is a static demo. In accordance with identity and security rules, no personal details are stored, logged, or sent across any network.
          </div>
          <button id="close-demo-modal" class="btn btn-primary" style="width: 100%;">Close Notification</button>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
    document.getElementById('close-demo-modal').addEventListener('click', () => {
      const modal = document.getElementById('demo-response-modal');
      if (modal) modal.remove();
    });
  };

  // 1. General Contact Form
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      let isValid = true;
      const requiredInputs = contactForm.querySelectorAll('[required]');

      requiredInputs.forEach(input => {
        if (!input.value.trim()) {
          isValid = false;
          input.classList.add('is-invalid');
        } else {
          input.classList.remove('is-invalid');
        }
      });

      if (!isValid) {
        alert('Please complete all required fields marked with an asterisk (*).');
        return;
      }

      showDemoNotice(
        'Consultation Enquiry Received',
        'Thank you for submitting your enquiry. In an active deployment, our corporate advisory desk would review your request and get back within one business day.'
      );
      contactForm.reset();
    });
  }

  // 2. Careers Application Form
  const careersForm = document.getElementById('careers-form');
  if (careersForm) {
    careersForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      let isValid = true;
      const requiredInputs = careersForm.querySelectorAll('[required]');

      requiredInputs.forEach(input => {
        if (!input.value.trim()) {
          isValid = false;
          input.classList.add('is-invalid');
        } else {
          input.classList.remove('is-invalid');
        }
      });

      if (!isValid) {
        alert('Please complete all required fields.');
        return;
      }

      showDemoNotice(
        'Application Profile Submitted',
        'Your demo application has been processed. In a production environment, your candidate dossier would be routed to human resources.'
      );
      careersForm.reset();
    });
  }

  // 3. Multi-Step Consultation Wizard (book-consultation.html)
  const wizard = document.getElementById('consultation-wizard');
  if (wizard) {
    let currentStep = 1;
    const totalSteps = 6;
    const panels = wizard.querySelectorAll('.wizard-panel');
    const nodes = wizard.querySelectorAll('.wizard-step-node');
    const progressBar = wizard.querySelector('.wizard-progress-bar');

    const updateStep = (newStep) => {
      // Bounds check
      if (newStep < 1 || newStep > totalSteps) return;

      currentStep = newStep;

      // Update panels
      panels.forEach((p, idx) => {
        if (idx + 1 === currentStep) {
          p.classList.add('active');
        } else {
          p.classList.remove('active');
        }
      });

      // Update progress nodes
      nodes.forEach((node, idx) => {
        const stepNum = idx + 1;
        node.classList.remove('active', 'completed');
        if (stepNum === currentStep) {
          node.classList.add('active');
        } else if (stepNum < currentStep) {
          node.classList.add('completed');
        }
      });

      // Update progress line bar
      if (progressBar) {
        const pct = ((currentStep - 1) / (totalSteps - 1)) * 100;
        progressBar.style.width = `${pct}%`;
      }

      // Populate review step if entering Step 6
      if (currentStep === 6) {
        populateReviewStep();
      }

      // Scroll smoothly to wizard top
      wizard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    const validateStep = (step) => {
      const panel = wizard.querySelector(`.wizard-panel[data-step="${step}"]`);
      if (!panel) return true;

      let valid = true;
      const requiredFields = panel.querySelectorAll('[required]');
      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          valid = false;
          field.classList.add('is-invalid');
        } else {
          field.classList.remove('is-invalid');
        }
      });

      return valid;
    };

    const populateReviewStep = () => {
      const name = wizard.querySelector('#wiz-name')?.value || 'Not provided';
      const email = wizard.querySelector('#wiz-email')?.value || 'Not provided';
      const phone = wizard.querySelector('#wiz-phone')?.value || 'Not provided';
      const org = wizard.querySelector('#wiz-org')?.value || 'Not provided';
      const industry = wizard.querySelector('#wiz-industry')?.value || 'General / Unspecified';
      const size = wizard.querySelector('#wiz-size')?.value || 'Unspecified';
      const stage = wizard.querySelector('#wiz-stage')?.value || 'Operating';
      const service = wizard.querySelector('#wiz-service')?.value || 'Strategic Consulting';
      const challenge = wizard.querySelector('#wiz-challenge')?.value || 'No details specified';
      const format = wizard.querySelector('#wiz-format')?.value || 'Virtual Video Discussion';
      const prefDate = wizard.querySelector('#wiz-date')?.value || 'Flexible';
      const prefTime = wizard.querySelector('#wiz-time')?.value || 'Business Hours';

      const setReview = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.textContent = val;
      };

      setReview('rev-name', name);
      setReview('rev-email', email);
      setReview('rev-phone', phone);
      setReview('rev-org', org);
      setReview('rev-industry', industry);
      setReview('rev-size', size);
      setReview('rev-stage', stage);
      setReview('rev-service', service);
      setReview('rev-challenge', challenge);
      setReview('rev-format', format);
      setReview('rev-datetime', `${prefDate} (${prefTime})`);
    };

    // Button event listeners
    wizard.querySelectorAll('.wizard-next-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        if (validateStep(currentStep)) {
          updateStep(currentStep + 1);
        } else {
          alert('Please provide all required information before proceeding.');
        }
      });
    });

    wizard.querySelectorAll('.wizard-prev-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        updateStep(currentStep - 1);
      });
    });

    // Final Wizard Submission
    const submitBtn = wizard.querySelector('.wizard-submit-btn');
    if (submitBtn) {
      submitBtn.addEventListener('click', (e) => {
        e.preventDefault();
        showDemoNotice(
          'Consultation Request Recorded',
          'Your multi-step consultation brief has been compiled in demo mode. No data has been saved or scheduled.'
        );
        wizard.reset();
        updateStep(1);
      });
    }
  }
});
