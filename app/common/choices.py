from model_utils import Choices

TYPE_USER = Choices((0, 'admin', 'admin'), (1, 'customer', 'customer'))

TYPE_GENDER_USER = Choices(
    ("male", "Masculino"),
    ("female", "Feminino"),
)
