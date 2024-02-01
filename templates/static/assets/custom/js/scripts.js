document.addEventListener('DOMContentLoaded', function() {
    console.log('Script carregado com sucesso.');
  
    var buscaVariacoes = document.getElementById('select-variacoes');
    var variation_preco = document.getElementById('variation-preco');
    var variation_preco_promocional = document.getElementById('variation-preco-promocional');
  
    buscaVariacoes.addEventListener('change', function() {
      console.log('Seleção alterada.');
  
      var selectedIndex = this.selectedIndex;
  
      if (selectedIndex === -1) {
        console.error('Nenhuma opção selecionada.');
        return;
      } else {
        console.log('Opção selecionada:', selectedIndex);
      }
  
      var preco = this.options[selectedIndex].getAttribute('data-preco');
      var preco_promocional = this.options[selectedIndex].getAttribute('data-preco-promocional');
  
      console.log('Preço:', preco);
      console.log('Preço Promocional:', preco_promocional);
  
      // Atualizar os elementos de preço na página
  
      var variation_preco = document.getElementById('variation-preco');
      var variation_preco_promocional = document.getElementById('variation-preco-promocional');
  
      if (preco !== null || preco !== undefined) {
        variation_preco.innerHTML = preco;
      } else {
        variation_preco.innerHTML = '';
      }
  
      if (preco_promocional !== null && preco_promocional !== undefined) {
        variation_preco_promocional.innerHTML = preco_promocional;
      } else {
        variation_preco_promocional.innerHTML = preco;
        variation_preco.innerHTML = '';
      }
    });
  });