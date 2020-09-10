const quantity = document.getElementById('id_quantity');
const rate = document.getElementById('id_rate');
const total = document.getElementById('id_total');
total.value = total.value || 0;
const oninputvalue = (e) => {
ip1 = quantity.value | 0;
ip2 = rate.value | 0;
total.value = ip1 * ip2;
}
quantity.oninput = oninputvalue;
rate.oninput = oninputvalue;