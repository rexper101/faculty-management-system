
        }, 8000);
      }
    });
  });

  // ── Active nav highlight (fallback for Jinja) ───────────────────────
  const currentPath = window.location.pathname.split('/')[1];
  document.querySelectorAll('.sidebar-nav .nav-link').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (href.includes(currentPath) && currentPath) {
      link.classList.add('active');
    }
  });

  // ── Sortable table columns ──────────────────────────────────────────
  document.querySelectorAll('table').forEach(table => {
    const headers = table.querySelectorAll('thead th');
    headers.forEach((th, colIndex) => {
      th.setAttribute('data-sort', colIndex);
      th.style.cursor = 'pointer';
      th.addEventListener('click', () => {
        const tbody = table.querySelector('tbody');
        const rows  = Array.from(tbody.querySelectorAll('tr'));
        const asc   = th.dataset.order !== 'asc';
        th.dataset.order = asc ? 'asc' : 'desc';
        // Reset other headers
        headers.forEach(h => { if (h !== th) delete h.dataset.order; });
        rows.sort((a, b) => {
          const av = a.cells[colIndex]?.textContent.trim() || '';
          const bv = b.cells[colIndex]?.textContent.trim() || '';
          const an = parseFloat(av.replace(/[₹,]/g, ''));
          const bn = parseFloat(bv.replace(/[₹,]/g, ''));
          const compare = isNaN(an) || isNaN(bn) ? av.localeCompare(bv) : an - bn;
          return asc ? compare : -compare;
        });
        rows.forEach(r => tbody.appendChild(r));
        // visual indicator
        headers.forEach(h => h.querySelector('.sort-icon')?.remove());
        const icon = document.createElement('i');
        icon.className = `bi bi-chevron-${asc ? 'up' : 'down'} sort-icon ms-1`;
        icon.style.fontSize = '.7rem';
        th.appendChild(icon);
      });
    });
  });

  // ── Date input — prevent future dates where needed ─────────────────
  document.querySelectorAll('input[name="date_of_birth"]').forEach(el => {
    el.max = new Date().toISOString().split('T')[0];
  });

  // ── Auto-uppercase employee/dept codes ─────────────────────────────
  document.querySelectorAll('[name="department_code"], [name="employee_code"]').forEach(el => {
    el.addEventListener('input', function () {
      const pos = this.selectionStart;
      this.value = this.value.toUpperCase();
      this.setSelectionRange(pos, pos);
    });
  });

  // ── Pincode — digits only ───────────────────────────────────────────
  document.querySelectorAll('[name="pincode"]').forEach(el => {
    el.addEventListener('input', function () {
      this.value = this.value.replace(/\D/g, '');
    });
  });

  console.log('%cFacultyIS loaded ✓', 'color:#6366f1;font-weight:700;font-size:13px');
})();
