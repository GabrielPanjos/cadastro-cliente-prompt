-- Cria o banco de dados chamado 'school_universe'
# CREATE DATABASE c;

-- Seleciona o banco de dados 'school_universe' para uso
USE school_universe;

-- Remove as tabelas se existirem (ordem importa por causa das dependências)
# DROP TABLE IF EXISTS Pagamento;
DROP TABLE IF EXISTS Compra;
# DROP TABLE IF EXISTS Produto;
DROP TABLE IF EXISTS Clientes;

-- Tabela de clientes
CREATE TABLE Clientes (
    id_clientes INT AUTO_INCREMENT PRIMARY KEY,       -- ID único com incremento automático
    nome VARCHAR(255) NOT NULL,                        -- Nome completo do cliente
    cpf VARCHAR(11) UNIQUE NOT NULL,                   -- CPF sem formatação
    rg VARCHAR(20),                                    -- RG do cliente
    data_nascimento DATE,                              -- Data de nascimento
    numero_telefone VARCHAR(20),                       -- Número de telefone
    email VARCHAR(255),                                -- Email do cliente
    estado VARCHAR(100),                               -- Estado de residência
    cidade VARCHAR(100),                               -- Cidade de residência
    rua VARCHAR(255),                                  -- Nome da rua
    cep VARCHAR(10),                                   -- CEP
    bairro VARCHAR(100),                               -- Bairro
    complemento VARCHAR(255),                          -- Complemento (ex: apto, bloco)
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Data de cadastro automática
);


-- Tabela de produtos disponíveis
CREATE TABLE Produto (
    `id_produto` INT AUTO_INCREMENT PRIMARY KEY,       -- ID do produto
    `nome` VARCHAR(255) NOT NULL,                      -- Nome do produto
    `marca` VARCHAR(255) NOT NULL,                     -- Marca do produto
    `preco` DECIMAL(10,2) NOT NULL,                    -- Preço do produto
    `quantidade_estoque` INT NOT NULL DEFAULT 0        -- Quantidade disponível em estoque
);



INSERT INTO Produto (nome, marca, preco) VALUES 
('Lápis Preto HB', 'Faber-Castell', 1.50),
('Caneta Azul', 'BIC', 2.00),
('Caderno 10 matérias', 'Tilibra', 18.90),
('Borracha Branca', 'Mercur', 1.20),
('Apontador com depósito', 'Maped', 3.50),
('Mochila Escolar', 'Sestini', 89.90),
('Estojo Grande', 'Capricho', 19.90),
('Régua 30cm', 'Trident', 2.50),
('Tesoura Escolar', 'Mundial', 4.99),
('Cola Branca 90g', 'Pritt', 2.99),
('Marca Texto', 'Faber-Castell', 3.99),
('Canetinha Hidrocor', 'Faber-Castell', 12.50),
('Caderno de Desenho', 'Tilibra', 15.00),
('Bloco de Anotações', 'Chamex', 5.50),
('Papel Sulfite A4 (500 folhas)', 'Chamex', 24.90),
('Pasta com elástico', 'Dello', 4.00),
('Grafite 0.7mm', 'Pentel', 2.30),
('Compasso Escolar', 'Trident', 7.90),
('Transferidor', 'Trident', 3.00),
('Agenda Escolar', 'Tilibra', 14.50);


