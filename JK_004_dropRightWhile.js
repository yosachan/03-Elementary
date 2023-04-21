function dropRightWhile(array, predicate){
    const droppedArray = [...array];

    for(let i = array.length - 1; 0 <= i; i--){
        const value = array[i];
        if ( !predicate(value, i, array)){
            break;
        };
        droppedArray.pop();
    };

    return droppedArray;
}

const users = [
    {'user':'barrney', 'active':true},
    {'user':'fred', 'active':false},
    {'user':'pebbles', 'active':false}
];

const result = dropRightWhile(users, function(o) {
     return !o.active;
});

console.log(result);

console.log(users);

