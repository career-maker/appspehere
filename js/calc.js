/* Distributor earnings calculator (same formulas as the live site) */
(function () {
  var shops = document.getElementById('shops'), sales = document.getElementById('sales'), margin = document.getElementById('margin');
  if (!shops || !sales || !margin) return;
  var S = [2500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 50000, 60000, 70000, 80000, 90000, 100000];
  var M = [4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15];
  var outlay = 41300 + 250000;
  function inr(v) { return '₹' + Math.round(v).toLocaleString('en-IN'); }
  function set(id, v) { document.getElementById(id).textContent = v; }
  function calc() {
    var n = Number(shops.value), s = S[Number(sales.value)], m = M[Number(margin.value)];
    var daily = n * s, inc = daily * (m / 100), rec = inc > 0 ? outlay / inc : 0;
    set('shopsValue', n); set('salesValue', inr(s)); set('marginValue', m + '%');
    set('dailyIncome', inr(inc)); set('monthlyIncome', inr(inc * 30)); set('yearlyIncome', inr(inc * 365));
    set('dailySales', inr(daily)); set('monthlyTurnover', inr(daily * 30)); set('yearlyTurnover', inr(daily * 365));
    set('recoveryDays', rec < 1 ? 'Less than 1 Day' : Math.ceil(rec) + ' Days');
    set('roiValue', Math.round(inc * 365 / outlay * 100).toLocaleString('en-IN') + '%');
    [shops, sales, margin].forEach(function (r) { r.style.setProperty('--fill', ((r.value - r.min) / (r.max - r.min) * 100) + '%'); });
  }
  [shops, sales, margin].forEach(function (r) { r.addEventListener('input', calc); });
  calc();
})();
