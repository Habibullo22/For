const tg = window.Telegram.WebApp;
tg.ready();

const userId = tg.initDataUnsafe.user.id;

fetch(`https://YOUR-REPLIT-URL.repl.co/balance/${userId}`)
  .then(res => res.json())
  .then(data => {
    document.getElementById("balance").innerHTML = `
      💵 USDT: ${data.usdt}<br>
      💴 RUB: ${data.rub}<br>
      💰 UZS: ${data.uzs}
    `;
  });
