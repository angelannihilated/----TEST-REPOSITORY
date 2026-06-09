// Click Reset = SANDER RETURNS TO ORIGINAL STATE!
document.getElementById('reset-btn').addEventListener('click', () => {
  // Directly manipulate the sand div's CSS transform 
  document.querySelector('.sand').style.transition = '0.3s';
  document.querySelector('.sand').style.transform = 'translateX(0)';  
});
