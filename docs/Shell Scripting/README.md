# Commonly used Syntax

### Printing Hello to console
```bash
echo 'Hello'
```

### For Loop
```bash
for i in {1..50} ;
do
    echo $i
done
```

### While Loop
```bash
while [[ $i -le 100 ]] ; do
    echo $i
    (( i += 1 ))
done
```

### Accepting input from console
```bash
read name
echo "Welcome $name"
```

### 
