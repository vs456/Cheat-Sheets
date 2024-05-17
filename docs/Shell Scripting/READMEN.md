# Commonly used Syntax

### Printing Hello to console
echo 'Hello'

### For Loop
for i in {1..50} ;
do
    echo $i
done

### While Loop
while [[ $i -le 100 ]] ; do
    echo $i
    (( i += 1 ))
done

### Accepting input from console
read name
echo "Welcome $name"

### 
