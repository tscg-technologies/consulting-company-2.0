/**
 * CONSULTING COMPANY — INTERACTIONS SCRIPT
 * FAQ Accordion, Case Study Filters, Insights Search & Category Filters
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. FAQ Accordion Interaction
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isActive = item.classList.contains('active');
      
      // Close sibling items within the same accordion container
      const parentAccordion = item.closest('.accordion');
      if (parentAccordion) {
        const siblings = parentAccordion.querySelectorAll('.accordion-item');
        siblings.forEach(sibling => {
          sibling.classList.remove('active');
          const btn = sibling.querySelector('.accordion-header');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        });
      }

      // Toggle current
      if (!isActive) {
        item.classList.add('active');
        header.setAttribute('aria-expanded', 'true');
      } else {
        item.classList.remove('active');
        header.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // 2. Case Studies & Generic Filter Buttons
  const filterButtons = document.querySelectorAll('.filter-btn');
  const filterableItems = document.querySelectorAll('.filterable-item');

  if (filterButtons.length > 0 && filterableItems.length > 0) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        // Toggle active button
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.getAttribute('data-filter');

        filterableItems.forEach(item => {
          const itemCategory = item.getAttribute('data-category');
          if (category === 'all' || itemCategory === category || (itemCategory && itemCategory.includes(category))) {
            item.classList.remove('hidden');
          } else {
            item.classList.add('hidden');
          }
        });
      });
    });
  }

  // 3. Insights Article Search
  const searchInput = document.getElementById('insights-search');
  if (searchInput && filterableItems.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      
      filterableItems.forEach(item => {
        const titleEl = item.querySelector('.article-card-title, .card-title');
        const descEl = item.querySelector('.article-card-desc, .card-desc');
        const title = titleEl ? titleEl.textContent.toLowerCase() : '';
        const desc = descEl ? descEl.textContent.toLowerCase() : '';

        if (title.includes(query) || desc.includes(query)) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    });
  }
});
