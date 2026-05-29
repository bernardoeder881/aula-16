/*-- CHAVE PRIMÁRIA
ALTER TABLE tb_clientes
MODIFY COLUMN codigo_cliente INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_cliente);

ALTER TABLE tb_itens
MODIFY COLUMN codigo_item INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_item);

ALTER TABLE tb_pedidos
MODIFY COLUMN codigo_pedido INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_pedido);

ALTER TABLE tb_produtos
MODIFY COLUMN codigo_produto INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_produto);

-- CHAVE ESTRANGEIRA
ALTER TABLE tb_pedidos
ADD CONSTRAINT fk_codigo_cliente
FOREIGN KEY (codigo_cliente) REFERENCES tb_clientes(codigo_cliente);

ALTER TABLE tb_itens
ADD CONSTRAINT fk_codigo_pedido
FOREIGN KEY (codigo_pedido) REFERENCES tb_pedidos( codigo_pedido)

ALTER TABLE tb_itens
ADD CONSTRAINT fk_codigo_produto
FOREIGN KEY (codigo_produto) REFERENCES tb_produtos( codigo_produto)

*/


