def input_layer(word_idx):
    x = torch.zeros(vocab_size).float()
    x[word_idx] = 1.0
    return x



def train(num_epochs = INT, lr = float,embedding_size = INT):

    W1 = Variable(torch.randn(embedding_size, vocab_size).float(), requires_grad=True)
    W2 = Variable(torch.randn(vocab_size, embedding_size).float(), requires_grad=True)

    for epoch in range(num_epochs):
        loss_val = 0
        for data, target in dataset:
            x = Variable(input_layer(data)).float()
            y_true = Variable(torch.from_numpy(np.array([target])).long())

            z1 = torch.matmul(W1, x)
            z2 = torch.matmul(W2, z1)
        
            log_softmax = F.log_softmax(z2, dim=0)

            loss = NLLloss(log_softmax(1,-1), y_true)	
            loss_val += loss
            
            W1.data -= lr * W1.grad.data
            W2.data -= lr * W2.grad.data

           
        if epoch % 10 == 0:    
            print(f'Loss at epoch {epoch}: {loss_val/len(dataset)}')
            
