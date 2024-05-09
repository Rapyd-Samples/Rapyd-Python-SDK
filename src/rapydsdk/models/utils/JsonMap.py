class JsonMap:
    """
    A class decorator used to map adjusted attribute names to original JSON attribute names before a request,
    and vice versa after the request.

    Example:
    @JsonMapping({
        'adjusted_name': 'original_name',
        'adjusted_list': 'original_list'
    })
    class SomeClass(BaseModel):
        adjusted_name: str
        adjusted_list: List[OtherClass]

    Methods:
    - _map(self): Converts the object's attributes to a dictionary with mapped attribute names.
    - _unmap(cls, data): Creates an object instance from a dictionary with mapped attribute names.

    Attributes:
    - mapping: A dictionary specifying the mapping between adjusted attribute names and original JSON attribute names.
    """

    def __init__(self, mapping):
        self.mapping = mapping

    def __call__(self, cls):
        """
        Transform the decorated class with attribute mapping capabilities.
        """
        cls.__json_mapping = self.mapping

        def _map(self):
            """
            Convert the object's attributes to a dictionary with mapped attribute names.

            Returns:
                dict: A dictionary with mapped attribute names and values.
            """
            map = self.__json_mapping
            attribute_dict = vars(self)
            result_dict = {}

            for key, value in attribute_dict.items():
                if isinstance(value, list):
                    value = [v._map() if hasattr(v, "_map") else v for v in value]
                elif hasattr(value, "_map"):
                    value = value._map()
                mapped_key = map.get(key, key)
                result_dict[mapped_key] = value

            return result_dict

        @classmethod
        def _unmap(cls, mapped_data):
            """
            Create an object instance from a dictionary with mapped attribute names.

            Args:
                mapped_data (dict): A dictionary with mapped attribute names and values.

            Returns:
                cls: An instance of the class with attribute values assigned from the dictionary.
            """
            reversed_map = {v: k for k, v in cls.__json_mapping.items()}
            mapped_attributes = {}
            for key, value in mapped_data.items():
                mapped_key = reversed_map.get(key, key)
                mapped_attributes[mapped_key] = value

            return cls(**mapped_attributes)

        cls._map = _map
        cls._unmap = _unmap

        return cls
