const count = document.querySelector('.count');
const input = document.querySelector('input');

input.addEventListener('input', () => {
  count.innerHTML = input.value.length;
});