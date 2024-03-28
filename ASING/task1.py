'''
Прием на работу IT-специалиста – дело ответственное, нужно проверить навыки претендента как в программировании, так и
в знании алгоритмов. Нужно провести собеседование так, чтобы затратить как можно меньше времени, но не потерять в
 качестве.

Собеседование включает 2 этапа: претенденту выдается задание, затем он идет его выполнять, представляет результат и
защищает его; потом претенденту дается 5 единиц времени отдохнуть; затем такие же действия проводятся для второго
задания, кроме отдыха, разумеется.

Напишите асинхронную функцию interviews(), которая принимает произвольное число претендентов – кортежей вида:
(имя, время на подготовку 1 задания, время на защиту 1 задания, время подготовки 2 задания, время на защиту второго
задания)

Функция должна для каждого задания каждого претендента вывести строки:
при начале выполнения задания – <имя> started the <N> task.
при переходе к защите – <имя> moved on to the defense of the <N> task.
при окончании выполнения задания – <имя> completed the <N> task.
при начале отдыха перед вторым заданием – <имя> is resting.

Второе задание каждый претендент может получить только после выполнения первого.
'''
import time
import asyncio

async def user(user: tuple) -> None:
    COEFF = 0.01
    print(f'{user[0]} started the 1 task.')
    await asyncio.sleep(COEFF * user[1])
    print(f'{user[0]} moved on to the defense of the 1 task.')
    await asyncio.sleep(COEFF * user[2])
    print(f'{user[0]} completed the 1 task.')
    print(f'{user[0]} started the 2 task.')
    await asyncio.sleep(COEFF * user[3])
    print(f'{user[0]} moved on to the defense of the 2 task.')
    await asyncio.sleep(COEFF * user[4])
    print(f'{user[0]} completed the 2 task.')

async def interviews(*args) -> None:
    tasks = []
    for p in args:
        tasks.append(asyncio.create_task(user(p)))
    await asyncio.gather(*tasks)



data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)