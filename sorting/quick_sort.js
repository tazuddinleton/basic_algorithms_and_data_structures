

let array = [6,5,4,3,21,1];
quickSort(array, 0, array.length-1);
console.log(array);

function partition(array, start, end, pivot){
    while(start <= end){
        while(array[start] < pivot){
            start++;
        }
        
        while(array[end] > pivot){
            end--;
        }

        if(start <= end){
            let elem = array[start];
            array[start] = array[end];
            array[end] = elem;

            start++;
            end--;
        }
    }
    return start;
}

function quickSort(array, start, end){
    if(start >= end){
        return;
    }

    let pivot = array[parseInt((start+end)/2)];
    let index = partition(array, start, end, pivot);
    quickSort(array, start, index-1);
    quickSort(array, index, end);
}