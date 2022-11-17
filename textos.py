from collections import defaultdict, Counter

text_one = """
Não importa se você está criando uma cena para uma fotografia, um vídeo, um desenho ou uma pintura, você sempre vai querer que seu público te entenda. Afinal, de que serve uma imagem que ninguém entende, não é mesmo?

Uma boa iluminação de cena ajuda a transmitir com clareza uma ideia ou sensação, e dominar algumas técnicas pode te ajudar na hora de decidir como estará a luz no ambiente que você quer retratar.
Confira neste artigo:

    Direcione sua luz para pedir atenção
    Use luzes direcionadas para maior realismo
    Luzes naturais são confortáveis
    Conclusão

Pensando nisso, separei três técnicas que podem fazer toda a diferença nessa hora. Vamos conversar sobre:

    Ponto focal e direcionamento do foco de luz.
    Uso de foco de luz para criar a sensação de volume e tridimensionalidade.
    Como usar ao seu favor a imprevisibilidade da luz natural.

Direcione sua luz para pedir atenção

Uma boa história é feita tanto do que você mostra quanto do que você esconde. Afinal, qual é a graça de assistir um filme de suspense sabendo desde o começo quem é o assassino? Na hora de criar sua cena, lembre-se que nem todos os elementos precisam estar à vista, e muito menos em destaque. Esconder elementos nas sombras é sempre muito efetivo!

Da mesma maneira, é importante dar muito destaque para o que for mais importante e central. E não estou exagerando: a pessoa tem que bater o olho na sua cena e conseguir entender imediatamente o que é mais importante.
Desenho de um homem ajoelhado ao lado de uma cama beliche, passando a mmão em uma criança que dorme. Há outra criança na cama de cima. Existe um feiche de luz entrando e mostrando a silhueta de uma mulher.

Autoria: Pascal Campion

A luz é uma maneira muito fácil de dar esse destaque, o olhar é atraído naturalmente para os lugares mais iluminados ou de maior contraste. Colocando um holofote no seu lugar principal, toda a atenção fica ali e você ainda tem a vantagem de poder colocar outros elementos fora desse foco central, que mal serão notados.

Aliás, veja esse vídeo e conte quantas vezes a equipe de branco passou a bola. Você vai se surpreender com o resultado.

Contou? E percebeu o urso dançando?

Enquanto estamos prestando atenção no foco da cena, que é a bola de basquete, estamos também ignorando completamente a pessoa fantasiada dançando bem em frente aos nossos olhos! Esse é o imenso poder de um bom ponto focal.
Use luzes direcionadas para maior realismo

Como dito anteriormente, somos tão guiados pela força da luz que ela acaba até escondendo coisas completamente óbvias, como uma pessoa fantasiada dançando ou até mesmo um dinossauro que não existe de verdade. Foi a técnica que o filme Parque dos Dinossauros usou na década de 1990 para esconder a computação gráfica simples e sem o poder que temos hoje.
Tiranossauro Rex rugindo entre dois carros em uma cena noturna com chuva e uma luz artificial forte vinda de cima.

Autoria: cena do filme Jurassic Park

Esse dinossauro não é um robô, ele só existe no computador e tem pouquíssimos detalhes perto do que vemos no cinema atualmente. Então como é que ele parece mais realista do que muito CG de filme recente, que batemos o olho e identificamos imediatamente que são falsos?

Simples! Uma boa iluminação.

Repare como existe apenas uma fonte de luz na cena, vinda de um poste de luz acima do dinossauro. Isso ajuda em dois sentidos diferentes: primeiro, muitos detalhes estão escondidos nas sombras, fazendo com que seja mais difícil perceber inconsistências e texturas esquisitas.

Depois, essa luz que bate em um só lado do dinossauro faz com que ele tenha uma sensação de volume muito maior do que se a luz fosse mais natural e viesse de várias direções ao mesmo tempo, sem um foco claro.

Ainda existe um pequeno detalhe que ajuda a construir a cena: a chuva gera uma espécie de cortina que faz muitos detalhes sumirem.

Por outro lado, temos cenas de filmes mais recentes, como esse exemplo do Star Wars:
"""

text_two = """
O que é o Looker?

O Looker é uma plataforma robusta de Business Intelligence (BI) comprada pela Google em 2019, sendo capaz de explorar conceitos de aprendizado de máquina, visualização de dados e criação de relatórios. Uma ferramenta que interage muito bem com os produtos Google e é capaz de importar dados do Google Ads, Analytics, Youtube e até planilhas. Para fortalecer ainda mais o ecossistema, a Google optou por trazer o Data Studio para o guarda chuva Looker.
O que foi Data Studio?

Em 2016, a Google anunciou o Data Studio, uma ferramenta gratuita que possibilitava a criação de dashboards e relatórios, de maneira fácil, a partir de fontes de dados. Por ser um ferramenta da Google, não faltaria compatibilidade com os seus produtos, incluindo Google Analytics, Google Ads, planilhas e muito mais, porém, em outubro de 2022, o nome Data Studio teve seu fim, sendo renomeada para Looker Studio.
O que é o Looker Studio?

De forma objetiva, o Looker Studio basicamente é o novo nome para o Data Studio. Essa mudança não altera as características do antigo Data Studio, pois a ferramenta Looker Studio continuará sendo oferecida de forma gratuita, ou seja, a ferramenta continua a mesma!
"""


def analyse_frequency_letter_in_text(text):
    total_by_letter = Counter(text.lower())
    total_character_text_one = sum(total_by_letter.values())
    frequences_by_letter = [(letter, frequency / total_character_text_one)
                            for letter, frequency in total_by_letter.items()]
    proportions = Counter(dict(frequences_by_letter))
    most_commons_teen_text_one = proportions.most_common(10)
    for letter, porcent in most_commons_teen_text_one:
        print("{} => {:.2f}".format(letter, porcent * 100))


print("texto um")
analyse_frequency_letter_in_text(text_one)
print('texto dois')
analyse_frequency_letter_in_text(text_two)