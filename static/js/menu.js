document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileOverlay = document.getElementById('mobile-overlay');

  function openMenu() {
    mobileMenu.classList.remove('translate-x-full');
    mobileOverlay.classList.remove('opacity-0', 'pointer-events-none');
    mobileOverlay.classList.add('opacity-100');
  }
  function closeMenu() {
    mobileMenu.classList.add('translate-x-full');
    mobileOverlay.classList.add('opacity-0', 'pointer-events-none');
    mobileOverlay.classList.remove('opacity-100');
  }

  if (menuToggle && mobileMenu && mobileOverlay) {
    menuToggle.addEventListener('click', openMenu);
    mobileOverlay.addEventListener('click', closeMenu);
  }
});
