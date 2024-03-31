import extended_queue

# Create an instance of ExtendedQueue
eq = extended_queue.ExtendedQueue(size=3, name="TestQueue")

try:
    eq.enqueue(1)
    eq.enqueue(2)
    eq.enqueue(3)
    print("Enqueued items successfully.")
except extended_queue.oo.QueueOutOfRangeException as e:
    print("Error:", e)

try:
    eq.enqueue(4)
    print("Enqueued additional item successfully.")
except extended_queue.oo.QueueOutOfRangeException as e:
    print("Error:", e)

print("Number of objects in queues:", eq.number_of_objects())

eq.save("queues.txt")
new_eq = extended_queue.ExtendedQueue(size=2, name="NewQueue")
new_eq.save("queues.txt")
extended_queue.ExtendedQueue.load("queues.txt")
print("Number of objects in queues after loading:", new_eq.number_of_objects())
