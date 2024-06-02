# Applied linear algebra
## Summary
### Talking about transformation matrices 2x2.
```
[a b]
[c d]
```
Element 𝑎: affects the scaling and rotation along the x-axis.

Element 𝑏, 𝑐:  contribute to the shearing effect. If ones are placed on b, c coordinates (x,y) -> (y,x)

Element 𝑑: affects the scaling and rotation along the y-axis.
### CV2 vs custom transformation functions
One key aspect of using cv2 for transformations is the requirement for the input matrix shape in the **cv2.transform** function. Specifically, cv2.transform expects the input matrix to be in the shape (1, a, b). So, this is because of frequently reshaping the input matrix to meet this requirement.
#### Shearing
Custom shearing and shearing in cv2 require different matrices to produce the same result
**Custom**
```
 def shear(self, axis:str, angle:float):
        angle = np.radians(angle)
        matrix = np.eye(2)
        if axis == 'x':
            matrix[1][0] = np.tan(angle)
        elif axis == 'y':
            matrix[0][1] = np.tan(angle)
        else:
            raise ValueError("incorrect axis")
        new_coordinates = self.coordinates @ matrix
        self.print_object(new_coordinates, "shear")
        return new_coordinates
```
**CV2**
```
def shear(self, axis:str, angle:float):
        angle = np.radians(angle)
        shear_matrix = np.eye(3)
        if axis == 'x':
            shear_matrix[0][1] =  np.tan(angle)
        elif axis == 'y':
            shear_matrix[1][0] =  np.tan(angle)
        else:
            raise ValueError("incorrect axis")
        new_coordinates = cv2.transform(self.coordinates,shear_matrix)[0]
        self.print_object(new_coordinates, "shear")
        return new_coordinates
```

Other transformations have the same matrices in cv2 and in custom functions 

# Відповіді на запитання

## Що таке лінійні трансформації?

Лінійні трансформації - це лінійні відображення векторів, що зберігають такі властивості як комутативність та множення на скаляр.

## Як і в яких галузях застосовуються лінійні трансформації?

- Криптографія (для кодування та розкодування, стиснення інформації)
- Комп'ютерний зір (рух зображень, імітація 3D)
- Машинне навчання (репрезентація зображень через вектори, різні маніпуляції з даними)

## Що таке матриця лінійної трансформації та як її можна інтерпретувати?

Матриця лінійної трансформації - це квадратна матриця, в якій кожен елемент відповідає за певне перетворення вихідної матриці. Множення цієї матриці на вихідну дозволяє отримати лінійно трансформовану матрицю.

## Які особливості та властивості має матриця обертання?

- det = 1
- Не змінює саме зображення (всі кути, пропорції та розмірності зберігаються)

## Чи залежить фінальний результат від порядку трансформацій?

Так, фінальний результат може залежати від порядку трансформацій, оскільки порядок множення матриць є важливим (некомутативність). Проте для деяких перетворень, таких як масштабування та обертання, порядок може не мати значення, особливо, якщо масштабування застосовується однаково по всіх осях.

**Результати експерименту можна знайти у файлі custom_transformations.**

**Висновок:** Якщо фактор масштабування є однаковим, то порядок не важливий. Проте це радше виняток. Адже як і для більшості трансформацій порядок стає важливим, як тільки фактори масштабування стають різними.

## Як знайти матрицю оберненої лінійної трансформації та чи завжди можна її знайти?

Матрицю оберненої лінійної трансформації можна знайти, якщо визначник матриці трансформації не дорівнює нулю. У цьому випадку можна знайти обернену матрицю до вихідної матриці трансформації і домножити її справа на отриману матрицю внаслідок перетворення.

## Які висновки можна зробити про трансформацію в залежності від модуля визначника матриці?

Фактор масштабування площі/об'єму = |det A|

- Якщо менше 1: площа/об'єм зменшується.
- Якщо = 1: площа/об'єм залишається незмінним.
- Якщо більше 1: площа/об'єм збільшується.
- Якщо = 0: розмірність простору, на який відбувається трансформація, зменшується. Відповідно, неможливо робити висновки, не знаючи, яке саме перетворення було виконано.

