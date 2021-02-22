var result = 0;
result = Math.random();
result = result*100;
result = result % 6;
result = Math.trunc(result);
document.write(result+1);