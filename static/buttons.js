document.addEventListener('DOMContentLoaded', () => {
  const cam = document.getElementById('cam');
  cam.addEventListener('click', () => {
    window.location.href = '/cam';
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const dashboard = document.getElementById('dashboard');
  dashboard.addEventListener('click', () => {
    window.location.href = '/dashboard';
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const mainpage = document.getElementById('mainpage');
  mainpage.addEventListener('click', () => {
    window.location.href = '/';
  });
});
