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

  