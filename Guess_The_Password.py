import random
import datetime
import time
from termcolor import colored as cl


gen_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$#@%&.0123456789"


print(cl('\nHi my name is CPU\U0001F600\nand I hope to guess the password witch in your mind\n',
      'cyan', attrs=['bold']))
time.sleep(2)
print(cl(f"\nSOOO I want you to write your password below\U0001F447\nBut don't worry I can't see it \U0001F5FF\n",
      'green', attrs=['bold']))
time.sleep(2)


def give_password():
    target = input(
        cl(f'plese insert your password \U0001F449:', 'yellow', attrs=['bold']))
    print(cl('\nOH give me secend to find it \U0001f914\n',
          'red', attrs=['bold']))
    time.sleep(1)
    return target


def generate_parent(length):
    genes = []
    while (len(genes) < length):
        sample_size = min(length - len(genes), len(gen_set))
        genes.extend(random.sample(gen_set, sample_size))
    return ''.join(genes)


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target_pass, guess)
               if expected == actual)


def mutate(parent):
    index = random.randrange(0, len(parent))
    child_genes = list(parent)
    new_gene, alternate = random.sample(gen_set, 2)
    child_genes[index] = alternate \
        if new_gene == child_genes[index] \
        else new_gene
    return ''.join(child_genes)


def display(guess):
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(time_diff)))


random.seed()
start_time = datetime.datetime.now()
target_pass = give_password()
best_parent = generate_parent(len(target_pass))
best_fitness = get_fitness(best_parent)
display(best_parent)
num_of_trys = 0
num_of_displays = 0


while True:
    child = mutate(best_parent)
    child_fitness = get_fitness(child)
    if child_fitness < best_fitness:
        num_of_trys += 1
        continue
    display(child)
    num_of_displays += 1
    if child_fitness >= len(best_parent):
        print(cl(
            f'\nYour password is "{child}" \U0001F60F\nAnd I find that after {num_of_trys} times guess\U0001F634\nBut I display my guess {num_of_displays} times\U0001F60E', 'red', attrs=['bold']))
        break
    best_fitness = child_fitness
    best_parent = child
