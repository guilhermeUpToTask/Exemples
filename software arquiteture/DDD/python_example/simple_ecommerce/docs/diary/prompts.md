Estou construindo um projeto de e-commerce seguindo DDD (Domain-Driven Design) inspirado no livro do Eric Evans.
Contexto atual do catálogo de produtos:

Entities vs Value Objects

Product é uma Entity com identidade (id) e atributos (name, category, price, description). Regras que dependem da entidade inteira ficam nela.

Price, ProductName e CategoryName são Value Objects: imutáveis, comparados por valor, encapsulam validações de cada atributo (ex: preço ≥ 0, nome não vazio, categoria válida).

Regras que envolvem múltiplas entidades ou agregados vão em Domain Services (ex: verificar estoque antes de criar pedido).

Repositories

No domínio: apenas interfaces/contratos (ProductRepository) definindo add, remove, get_by_id, list_all.

Na infraestrutura: implementação concreta (ex: SQLModel).

Permite testes do domínio sem acessar banco.

Application Services

Orquestram casos de uso, chamam entidades, VOs e repositórios, mas não contêm regras de negócio puras.

Exemplo: RegisterProductService cria produto chamando Product + VOs + repository.

Domain Services

Para regras envolvendo múltiplas entidades ou agregados.

Exemplo: StockCheckerService verifica disponibilidade de produtos antes de criar pedido.

Organização de arquivos de Value Objects

src/domain/catalog/value_objects/
├── price.py          # Price VO + regras
├── product_name.py   # ProductName VO + regras
├── category_name.py  # CategoryName VO + regras


Evitar arquivos genéricos como product_rules.py.

Mantém coesão, testabilidade e domínio puro.

Princípios DDD aplicados

Domínio independente de infra (FastAPI, SQLModel, Pydantic).

Regras perto do dado: VOs e Entities encapsulam regras.

Contracts first: Repositórios apenas definem interfaces.

Testabilidade: mocks/fakes facilitam testes sem DB.