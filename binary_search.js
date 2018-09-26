function bSearch(arr, e) {
  var l = 0;
  var r = arr.length;
  if (l == r) {
    return -1;
  }

  while (l < r) {
    var m = parseInt((l + r) / 2);
    if (arr[m] == e) {
      return m;
    }
    if (arr[m] > e) {
      r = m;
    }
    if (arr[m] < e) {
      l = m + 1;
    }
    return -1;
  }
}

var arr = [1, 3, 4, 6, 7, 8];
var e = 0;
var i = bSearch(arr, e);

console.log(i);
