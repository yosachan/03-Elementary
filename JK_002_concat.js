function concat(array, ...values){
    const concatedArray = [...array];
    for(let i=0; i<values.length; i++){
        const value = values[i];
        if(Array.isArray(value)){
            concatedArray.push(...value);
        }else{
            concatedArray.push(value);
        }
    }

    return concatedArray;
}

const array = [1];
const other = concat(array, 2, [3], [[4]]);

console.log(other);
console.log(array);
















