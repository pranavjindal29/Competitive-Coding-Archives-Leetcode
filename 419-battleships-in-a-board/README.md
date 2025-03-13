<h2><a href="https://leetcode.com/problems/battleships-in-a-board">Battleships in a Board</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an <code>m x n</code> matrix <code>board</code> where each cell is a battleship <code>&#39;X&#39;</code> or empty <code>&#39;.&#39;</code>, return <em>the number of the <strong>battleships</strong> on</em> <code>board</code>.</p>

<p><strong>Battleships</strong> can only be placed horizontally or vertically on <code>board</code>. In other words, they can only be made of the shape <code>1 x k</code> (<code>1</code> row, <code>k</code> columns) or <code>k x 1</code> (<code>k</code> rows, <code>1</code> column), where <code>k</code> can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img height="333" src="https://assets.leetcode.com/uploads/2024/06/21/image.png" width="333" />
<pre>
<strong>Input:</strong> board = [[&quot;X&quot;,&quot;.&quot;,&quot;.&quot;,&quot;X&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;X&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;X&quot;]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = [[&quot;.&quot;]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is either <code>&#39;.&#39;</code> or <code>&#39;X&#39;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it in one-pass, using only <code>O(1)</code> extra memory and without modifying the values <code>board</code>?</p>
