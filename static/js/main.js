/* ═══════════════════════════════════════════════════════════════════════
   Faculty Information System — Main JS
   ═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── Sidebar toggle ─────────────────────────────────────────────────
  const sidebar      = document.getElementById('sidebar');
  const mainWrapper  = document.getElementById('mainWrapper');
  const overlay      = document.getElementById('sidebarOverlay');
  const toggleBtn    = document.getElementById('sidebarToggle');
  const closeBtn     = document.getElementById('sidebarClose');

  function openSidebar() {
    sidebar?.classList.add('open');
    overlay?.classList.add('show');
  }

  function closeSidebar() {
    sidebar?.classList.remove('open');
    overlay?.classList.remove('show');
  }

  toggleBtn?.addEventListener('click', () => {
    if (window.innerWidth >= 992) {
      // Desktop: collapse/expand
      const collapsed = mainWrapper.style.marginLeft === '0px';
      mainWrapper.style.marginLeft = collapsed ? 'var(--sidebar-width)' : '0px';
      sidebar.style.transform      = collapsed ? 'none' : 'translateX(-100%)';
    } else {
      openSidebar();
    }
  });

  closeBtn?.addEventListener('click', closeSidebar);
  overlay?.addEventListener('click', closeSidebar);

  // Close sidebar on resize to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 992) closeSidebar();
  });

  // ── Auto-dismiss flash alerts after 5s ─────────────────────────────
  document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert?.close();
    }, 5000);
  });

  // ── Confirm on delete forms (fallback) ─────────────────────────────
  document.querySelectorAll('form[data-confirm]').forEach(form => {
    form.addEventListener('submit', e => {
      if (!confirm(form.dataset.confirm)) e.preventDefault();
    });
  });

  // ── Salary net calculator (on any page that may have it) ───────────
  function calcSalaryNet() {
    const basic  = parseFloat(document.getElementById('basic')?.value) || 0;
    const allow  = parseFloat(document.getElementById('allowances')?.value) || 0;
    const deduct = parseFloat(document.getElementById('deductions')?.value) || 0;
    const el     = document.getElementById('netDisplay');
    if (el) el.textContent = '₹' + (basic + allow - deduct).toFixed(2);
  }
