from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import TodoItem


# Create your tests here.
def createItem(client):
    url = reverse('todoitem-list')
    data = {'title': 'Walk the dog'}
    return client.post(url, data, format='json')

# Classes used for each major test
class TestCreateTodoItem(APITestCase):
    """
    Ensure we can create a new todo item
    """

    # Setup the test
    def setUp(self):
        self.response = createItem(self.client)
    
    # Did it acknowledge it created the item?
    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code , status.HTTP_201_CREATED)

    # Did it properly return a location header?  (matches pattern http://<ANYTHING>/todos/<INTEGER>)
    def test_received_location_header_hyperline(self):
        self.assertRegexpMatches(self.response['Location'], '^http://.+/todos/[\d]+$')
    
    # Did it properly return a TodoItem?
    def test_item_was_created(self):
        self.assertEqual(TodoItem.objects.count(), 1)
    
    # Did the TodoItem have the appropriate title?
    def test_item_has_correct_title(self):
        self.assertEqual(TodoItem.objects.get().title, 'Walk the dog')

class TestUpdateTodoItem(APITestCase):
    """
    Ensure we can update an existing todo item using PUT
    """
    
    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TodoItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Walkd the dog', 'completed': True}
        self.response = self.client.put(url, data, format='json')
    
    def test_received_200_ok_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(TodoItem.objects.get().completed, True)

class TestPatchTodoItem(APITestCase):
    """
    Ensure we can update an existing todo item using PATCH
    """
    
    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TodoItem.objects.get().completed, False)
        url = response['Location']
        data = {'title': 'Walk the dog', 'completed': True}
        self.response = self.client.patch(url, data, format='json')

    def test_received_200_ok_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(TodoItem.objects.get().completed, True)

class TestDeleteTodoItem(APITestCase):
    """
    Ensure we can delete a todo item
    """

    def setUp(self):
        response = createItem(self.client)
        self.assertEqual(TodoItem.objects.count(), 1)
        url = response['Location']
        self.response = self.client.delete(url)

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_the_item_was_deleted(self):
        self.assertEqual(TodoItem.objects.count(), 0)
