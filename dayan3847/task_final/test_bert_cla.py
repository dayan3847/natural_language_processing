import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset


# Definir la clase del dataset personalizado
class SpamDataset(Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=128,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

        input_ids = encoding["input_ids"].squeeze()
        attention_mask = encoding["attention_mask"].squeeze()

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "label": torch.tensor(label)
        }


# Cargar el tokenizer y el modelo preentrenado de BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Cargar tus datos de spam y ham desde la base de datos
texts = [...]  # Lista de textos de tus datos
labels = [...]  # Lista de etiquetas (0 para ham, 1 para spam)

# Crear el dataset personalizado
dataset = SpamDataset(texts, labels, tokenizer)

# Dividir los datos en conjuntos de entrenamiento y validación
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

# Definir el dataloader para el entrenamiento y la validación
batch_size = 16
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Configurar el entrenamiento del modelo
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
num_epochs = 5

# Entrenar el modelo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

for epoch in range(num_epochs):
    model.train()
    train_loss = 0.0

    for batch in train_dataloader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["label"].to(device)

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        train_loss += loss.item()

        loss.backward()
        optimizer.step()

    avg_train_loss = train_loss / len(train_dataloader)

    model.eval()
    val_loss = 0.0
    correct_predictions = 0

    with torch.no_grad():
        for batch in val_dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["label"].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            logits = outputs.logits

            val_loss += loss.item()

            predictions = torch.argmax(logits, dim=1)
    correct_predictions += torch.sum(predictions == labels)

    avg_val_loss = val_loss / len(val_dataloader)

    print("Accuracy: {}".format(correct_predictions.double() / len(val_dataset)))
    print("Training loss: {}".format(avg_train_loss))
    print("Validation loss: {}".format(avg_val_loss))

# Guardar el modelo entrenado
torch.save(model.state_dict(), "model.pth")
