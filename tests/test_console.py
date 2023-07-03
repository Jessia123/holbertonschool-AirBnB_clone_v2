def test_create_with_parameters(self):
    # Simulate the create command with parameters
    self.console.onecmd('create BaseModel name="My_little_house" value=3.14')

    # Retrieve the newly created object from the storage
    obj = models.storage.all()["BaseModel.{}".format(self.console.obj.id)]

    # Verify that the object has been created with the correct attributes
    self.assertEqual(obj.name, "My little house")
    self.assertEqual(obj.value, 3.14)
