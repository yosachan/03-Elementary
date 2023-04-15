function chunk(array, size=1){
    if(size < 0){
        throw new Error('第2引数は1以上でなければならない');
    }
    chunkedArray = [];
    copiedArray = [...array];
    while(copiedArray.length > 0){
        const splicedValues = copiedArray.splice(0, size);
        chunkedArray.push(splicedValues);
    }
    return chunkedArray;
}

const chrList = ['a', 'b', 'c', 'd'];

console.log(chunk(chrList, 2));
console.log(chunk(chrList, 0));

















