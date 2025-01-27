const checkLotNumbers: (entried?: string | number) => void = (entried?: string | number) => {
    const _checkLotResult: (changeTypeNum_Number: number) => void = (changeTypeNum_Number: number) => {
        if (changeTypeNum_Number === 123456) {
            console.log(`${changeTypeNum_Number} is a Special Prize!`);
            console.log('Great!');
            return;
        }

        const changeTypeNum_Str: string = changeTypeNum_Number.toString();
        const last4_Chars: string = changeTypeNum_Str.slice(changeTypeNum_Str.length - 4, changeTypeNum_Str.length);
        const last2_Chars: string = changeTypeNum_Str.slice(changeTypeNum_Str.length - 2, changeTypeNum_Str.length);
        // console.log(changeTypeNum_Str, last4_Chars, last2_Chars);

        if (last4_Chars === '7890') {
            console.log(`${changeTypeNum_Str} is 2nd prize.`);
        } else if (last2_Chars === '05') {
            console.log(`${changeTypeNum_Str} is 3rd prize.`);
        } else {
            console.log('no prize.');
        }
    }

    if (typeof entried !== 'number') {
        // const changeTypeNum_Number: number = Number(entried);
        const changeTypeNum_Number: number = typeof entried !== 'undefined' ? parseInt(entried) : 0;

        if (!isNaN(changeTypeNum_Number)) {
            _checkLotResult(changeTypeNum_Number);
        } else {
            console.log(`${entried} is type:[${typeof (entried)}].\n we accept only NUMBER.`);
        }
    } else if (typeof entried !== undefined) {
        _checkLotResult(entried);
    }
}

checkLotNumbers(123456);
checkLotNumbers('123456');
checkLotNumbers(458527890);
checkLotNumbers('458527890');
checkLotNumbers(123405);
checkLotNumbers('1234-05');
checkLotNumbers('1234.05');
checkLotNumbers(1234.05);
