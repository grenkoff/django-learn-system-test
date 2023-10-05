# Project `django-learn-system-test`

This project is a test task for HardQode.

## Test task

Execution time ~ 8 hours for a junior level
Submission deadline - within 4 days

## Building a learning system

The essence of the task is to test knowledge of building database relationships and the ability to construct queries without N+1 errors.

Before starting the task, we recommend studying the materials that will help with the tasks:
https://docs.djangoproject.com/en/4.2/intro/tutorial01/
https://docs.djangoproject.com/en/4.2/topics/db/models/
https://docs.djangoproject.com/en/4.2/topics/db/queries/
https://docs.djangoproject.com/en/4.2/ref/models/querysets/
https://www.django-rest-framework.org/tutorial/quickstart/
https://www.django-rest-framework.org/api-guide/viewsets/
https://www.django-rest-framework.org/api-guide/serializers/

### Architecture design (3 points)

In this task, we have three business tasks for storage:
1. Create a product entity. The product should have an owner. It is necessary to add an entity to save access to the product for the user.
2. Create a lesson entity. A lesson can be in multiple products at the same time. The lesson should have basic information: title, video link, viewing duration (in seconds).
3. Many users can view the lesson. It is necessary to record the viewing time for each user and the status "Viewed"/"Not viewed". The "Viewed" status is set if the user has watched 80% of the video.

### Query writing (7 points)

In this section, you will need to use the architecture you created in the previous task:
1. Implement an API to display a list of all lessons across all products to which the user has access, including information about the status and viewing time.
2. Implement an API to display a list of lessons for a specific product to which the user has access, including information about the status and viewing time, as well as the date of the last viewing of the video.
3.  Implement an API to display product statistics. It is necessary to display a list of all products on the platform, and for each product, attach the following information:
* The number of viewed lessons by all students.
* The total time all students spent watching the videos.
* The number of students studying the product.
* The product acquisition percentage (calculated based on the number of accesses to the product divided by the total number of users on the platform).

### Execution result

1. Implemented architecture based on SQLite database using Django.
2. Implemented APIs based on the prepared architecture.

### We expect

A link to a public GitHub repository with the completed project.