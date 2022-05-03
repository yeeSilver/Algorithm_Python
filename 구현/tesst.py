function mul(num){
	if (num === 1) return 1;
	return num * mul(num-1);
}
mul(5)
print(5*4*3*2*1)
print(mul(5))
