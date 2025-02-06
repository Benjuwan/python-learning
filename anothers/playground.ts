// 入力した内容によって出力結果が変わる（数値の場合は宝くじ： 完全一致や下4桁、下2桁などで分岐）
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

// 引数に指定した文字列配列内の各文字列における「文字列内での重複文字と重複回数」をチェックする処理
type checkDuplicateWordAndCounts_resultType = {
    chars: string;
    char: string;
    count: number;
}

const checkDuplicateWordAndCounts: (theWords: string[]) => checkDuplicateWordAndCounts_resultType[] = (
    theWords: string[]
) => {
    const results: checkDuplicateWordAndCounts_resultType[] = [];

    for (const theWord of theWords) {
        // 各文字の出現回数を記録するマップを作成
        const charsMap: Map<string, number> = new Map<string, number>();

        // 文字列内の各文字の出現回数をカウント
        for (const char of theWord) {
            // 第二引数部分の処理： char がまだ存在しない（falseの）場合は 0を指定し、既に存在する場合は取得した char の値（既存の値）に +1する
            charsMap.set(char, (charsMap.get(char) || 0) + 1);
        }

        let theChar: string = '';
        let theCount: number = 0;

        // エントリー（[key, value]のペア）を取得
        for (const [char, count] of charsMap.entries()) {
            // 文字が切り替わったら重複計測回数（theCount）を初期化
            if (theChar !== char) {
                theCount = 0;
            }

            // 重複計測回数（theCount）より大きい（＝重複している）場合は購読開始
            if (count > theCount) {
                theChar = char;
                theCount = count;
            }

            // 重複がある場合のみ（出現回数が2回以上）結果に追加
            if (theCount >= 2) {
                const newResult: checkDuplicateWordAndCounts_resultType = {
                    chars: theWord,
                    char: theChar,
                    count: theCount
                }
                results.push(newResult);
            }
        }
    }

    return results;
}

const targetStrAry: string[] = ["beer", "www", "apple", "banana", "soda", "benjuwan jijao"];

const theCheckDuplicateWordAndCounts: checkDuplicateWordAndCounts_resultType[] = checkDuplicateWordAndCounts(targetStrAry);
// console.log(theCheckDuplicateWordAndCounts);

// ソート処理（別に不要）
const sort_theCheckDuplicateWordAndCounts = [...theCheckDuplicateWordAndCounts].sort((
    a: checkDuplicateWordAndCounts_resultType,
    b: checkDuplicateWordAndCounts_resultType
) => {
    if (a.chars > b.chars) {
        return 1; // 昇順（ask）
    } else {
        return -1; // 降順（desk）
    }
});
console.log(sort_theCheckDuplicateWordAndCounts);