const a=document.getElementById('totalIncome');
const b=document.getElementById('totalExpenses');
const c=document.getElementById('totalBalance');
const d=document.getElementById('message');
const e=document.getElementById('form');
const f=document.getElementById('name');
const g=document.getElementById('amount');
const h=document.getElementById('transactionType');
const i=document.getElementById('transactionCategory');
const j=document.getElementById('list');

let transactions=[];

let savedTransactions=localStorage.getItem('transactions');

if(savedTransactions){
    transactions=JSON.parse(savedTransactions);
}

e.addEventListener("submit",addTransaction);
function addTransaction(event){
    event.preventDefault();
    const name = f.value.trim();
    const amount =Number(g.value);
    const transactionCategory = i.value;
    const transactionType = h.value;

    if(name==="" || amount<=0){
        d.textContent="Please enter valid name and amount";
        return;
    }
    const transaction={
        id:Date.now(),
        name: name,
        amount:amount,
        transactionType:transactionType,
        transactionCategory:transactionCategory
    
};

transactions.push(transaction);

savedTransaction();

renderTransactions();

   e.reset();

   d.textContent="Transaction added successfully";

}

function renderTransactions( transactionArray = transactions){

    j.innerHTML = "";

    transactionArray.forEach(function(transaction){
        const sign = transaction.transactionType === "income" ? "+": "-";
        const amountClass = transaction.TransactionType === "income"? "income-amount":"expense-amount";

        j.innerHTML += `
        <div class ="transaction">
            <div class="transaction-info">
            <h3>${transaction.name}</h3>
            <p>${transaction.transactionCategory}</p>
            </div>
            <div class = "transaction-amount">
            <span class="${amountClass}">
            ${sign} ${transaction.amount}
            </span>

            </div>
        </div>
    `;
    }
)
calculateTotals();
};
 function calculateTotals(){
    const income = transactions.filter(function(transaction){
        return transaction.transactionType ==="income";})
        .reduce(function(total, transaction){
            return total+transaction.amount;

},0);
    const expense = transactions.filter(function(transaction){
        return transaction.transactionType ==="expense";})
        .reduce(function(total, transaction){
            return total+transaction.amount;
},0);
const currentBalance = income - expense;

a.textContent = income;
b.textContent = expense;
c.textContent = currentBalance;
}

function savedTransaction(){
    localStorage.setItem("transaction",JSON.stringify(transactions));}

renderTransactions();