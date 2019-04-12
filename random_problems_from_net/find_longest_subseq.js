// var s1 = "ABAZDC";
// var s2 = "BACBAD";


var s1 = 'AGGTAB';
var s2 = 'GXTXAYB';
var results = [];
for (var i = 0; i < s1.length; i++) {
    results.push(longestSubseq(s1, s2, i));
}
function longestSubseq(s1, s2, startIndx) {
    var result = "";
    var s1Indx = 0;
    var s2Indx = 0;
    for (var i = 0; i < s1.length; i++) {
        var char = s1[i + startIndx];
        var indx = s2.substring(s2Indx, s2.length)
            .indexOf(char);
        if (indx >= s2Indx) {
            result += char
            s2Indx = indx;
        } else {

        }
    }
    return result;
}

function longestString(results) {
    var longest = "";
    for (var i = 0; i < results.length; i++) {
        if (results[i].length > longest.length) {
            longest = results[i];
        }
    }
    return longest;
}

console.log(results);
console.log(longestString(results));