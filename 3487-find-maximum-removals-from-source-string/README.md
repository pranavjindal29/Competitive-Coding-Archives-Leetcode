<h2><a href="https://leetcode.com/problems/find-maximum-removals-from-source-string">Find Maximum Removals From Source String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given a string <code>source</code> of size <code>n</code>, a string <code>pattern</code> that is a <span data-keyword="subsequence-string">subsequence</span> of <code>source</code>, and a <strong>sorted</strong> integer array <code>targetIndices</code> that contains <strong>distinct</strong> numbers in the range <code>[0, n - 1]</code>.</p>

<p>We define an <strong>operation</strong> as removing a character at an index <code>idx</code> from <code>source</code> such that:</p>

<ul>
	<li><code>idx</code> is an element of <code>targetIndices</code>.</li>
	<li><code>pattern</code> remains a <span data-keyword="subsequence-string">subsequence</span> of <code>source</code> after removing the character.</li>
</ul>

<p>Performing an operation <strong>does not</strong> change the indices of the other characters in <code>source</code>. For example, if you remove <code>&#39;c&#39;</code> from <code>&quot;acb&quot;</code>, the character at index 2 would still be <code>&#39;b&#39;</code>.</p>

<p>Return the <strong>maximum</strong> number of <em>operations</em> that can be performed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = &quot;abbaa&quot;, pattern = &quot;aba&quot;, </span>targetIndices<span class="example-io"> = [0,1,2]</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>We can&#39;t remove <code>source[0]</code> but we can do either of these two operations:</p>

<ul>
	<li>Remove <code>source[1]</code>, so that <code>source</code> becomes <code>&quot;a_baa&quot;</code>.</li>
	<li>Remove <code>source[2]</code>, so that <code>source</code> becomes <code>&quot;ab_aa&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = &quot;bcda&quot;, pattern = &quot;d&quot;, </span>targetIndices<span class="example-io"> = [0,3]</span></p>

<p><strong>Output:</strong> 2</p>

<p><strong>Explanation:</strong></p>

<p>We can remove <code>source[0]</code> and <code>source[3]</code> in two operations.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = &quot;dda&quot;, pattern = &quot;dda&quot;, </span>targetIndices<span class="example-io"> = [0,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>We can&#39;t remove any character from <code>source</code>.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">source = </span>&quot;yeyeykyded&quot;<span class="example-io">, pattern = </span>&quot;yeyyd&quot;<span class="example-io">, </span>targetIndices<span class="example-io"> = </span>[0,2,3,4]</p>

<p><strong>Output:</strong> 2</p>

<p><strong>Explanation:</strong></p>

<p>We can remove <code>source[2]</code> and <code>source[3]</code> in two operations.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == source.length &lt;= 3 * 10<sup>3</sup></code></li>
	<li><code>1 &lt;= pattern.length &lt;= n</code></li>
	<li><code>1 &lt;= targetIndices.length &lt;= n</code></li>
	<li><code>targetIndices</code> is sorted in ascending order.</li>
	<li>The input is generated such that <code>targetIndices</code> contains distinct elements in the range <code>[0, n - 1]</code>.</li>
	<li><code>source</code> and <code>pattern</code> consist only of lowercase English letters.</li>
	<li>The input is generated such that <code>pattern</code> appears as a subsequence in <code>source</code>.</li>
</ul>
